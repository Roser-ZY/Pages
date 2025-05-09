---
title: "本地缓存 Range 的实现方案"
author: "Roser"
date: 2025-05-09
image: "images/content/IndexedDB.png"
draft: false
tags:
  - IndexedDB
  - ChromeExtension
---
如果您想使用 IndexDB 来进行本地存储，而不再使用 `chrome.storage`，可以对原有方案进行以下修改：

**主要变更点**：

1. 在内容脚本中存储数据时，从使用 `chrome.storage.local` 改为使用 IndexDB 数据库操作来写入高亮数据。
2. 页面加载时，同样从 IndexDB 中读取对应 URL 的高亮数据并恢复高亮。

下面将展示一个示例流程和相应代码片段。请注意这是一个参考实现示例，实际开发中需要根据具体需求完善代码结构和异常处理。

一般在 [Service Worker](../../Chrome-Extension/Service-Worker-基础) 中使用 IndexedDB，此时不需要 `chrome.storage` 权限。

### 初始化 IndexDB

在您的扩展中编写一个辅助模块 `db.ts` 来封装 IndexDB 的打开和读写逻辑。假设我们使用一个名为 `"HighlightDB"` 的数据库和 `"highlights"` 的对象存储（object store），其中 key 是 URL，value 是该 URL 对应的一组高亮数据记录。

```typescript
// db.ts
export interface HighlightData {
  text: string;
  startContainerPath: number[];
  endContainerPath: number[];
  startOffset: number;
  endOffset: number;
}

const DB_NAME = 'HighlightDB';
const STORE_NAME = 'highlights';
const DB_VERSION = 1;

let dbPromise: Promise<IDBDatabase> | null = null;

function openDB(): Promise<IDBDatabase> {
  if (!dbPromise) {
    dbPromise = new Promise((resolve, reject) => {
      const request = indexedDB.open(DB_NAME, DB_VERSION);
      request.onupgradeneeded = (e) => {
        const db = request.result;
        if (!db.objectStoreNames.contains(STORE_NAME)) {
          db.createObjectStore(STORE_NAME, { keyPath: 'url' });
        }
      };
      request.onsuccess = () => resolve(request.result);
      request.onerror = () => reject(request.error);
    });
  }
  return dbPromise;
}

export async function saveHighlights(url: string, highlights: HighlightData[]): Promise<void> {
  const db = await openDB();
  return new Promise<void>((resolve, reject) => {
    const tx = db.transaction(STORE_NAME, 'readwrite');
    const store = tx.objectStore(STORE_NAME);
    store.put({ url, highlights });
    tx.oncomplete = () => resolve();
    tx.onerror = () => reject(tx.error);
  });
}

export async function getHighlights(url: string): Promise<HighlightData[]> {
  const db = await openDB();
  return new Promise<HighlightData[]>((resolve, reject) => {
    const tx = db.transaction(STORE_NAME, 'readonly');
    const store = tx.objectStore(STORE_NAME);
    const req = store.get(url);
    req.onsuccess = () => {
      if (req.result) {
        resolve(req.result.highlights || []);
      } else {
        resolve([]);
      }
    };
    req.onerror = () => reject(req.error);
  });
}
```

### 修改内容脚本

在内容脚本 `content_script.ts` 中，替换之前的 `chrome.storage` 存储代码为 IndexDB 的存储逻辑。

```typescript
// content_script.ts
import { saveHighlights, getHighlights, HighlightData } from './db';

document.addEventListener('mouseup', () => {
  const selection = window.getSelection();
  if (!selection || selection.rangeCount === 0) return;

  const range = selection.getRangeAt(0);
  const selectedText = selection.toString().trim();
  if (!selectedText) return;

  const currentUrl = window.location.href;

  const startContainerPath = getNodePath(range.startContainer);
  const endContainerPath = getNodePath(range.endContainer);
  const startOffset = range.startOffset;
  const endOffset = range.endOffset;

  const highlightData: HighlightData = {
    text: selectedText,
    startContainerPath,
    endContainerPath,
    startOffset,
    endOffset
  };

  // 先从DB中获取当前URL已有的高亮数据，然后加入新的，再保存回DB
  getHighlights(currentUrl).then(existingHighlights => {
    existingHighlights.push(highlightData);
    return saveHighlights(currentUrl, existingHighlights);
  }).catch(err => console.error("Failed to save highlights:", err));
});

window.addEventListener('DOMContentLoaded', () => {
  const currentUrl = window.location.href;
  getHighlights(currentUrl)
    .then(highlights => {
      highlights.forEach(data => restoreHighlight(data));
    })
    .catch(err => console.error("Failed to load highlights:", err));
});


function getNodePath(node: Node): number[] {
  const path: number[] = [];
  let current: Node | null = node;
  while (current && current.parentNode) {
    const parent = current.parentNode;
    const index = Array.prototype.indexOf.call(parent.childNodes, current);
    path.unshift(index);
    current = parent;
  }
  return path;
}

function getNodeFromPath(path: number[]): Node | null {
  let node: Node = document;
  for (const index of path) {
    if (!node.childNodes || index < 0 || index >= node.childNodes.length) {
      return null;
    }
    node = node.childNodes[index];
  }
  return node;
}

function restoreHighlight(data: HighlightData) {
  const startNode = getNodeFromPath(data.startContainerPath);
  const endNode = getNodeFromPath(data.endContainerPath);
  if (!startNode || !endNode) return;

  const range = document.createRange();
  try {
    range.setStart(startNode, data.startOffset);
    range.setEnd(endNode, data.endOffset);
  } catch (e) {
    console.error("Failed to set range:", e);
    return;
  }

  if (range.toString() !== data.text) {
    // 内容发生变化，不进行高亮
    return;
  }

  const span = document.createElement('span');
  span.style.color = 'red';
  range.surroundContents(span);
}
```

### manifest.json 不变

仍然使用 manifest v3 并加载 content_script 即可：

```json
{
  "manifest_version": 3,
  "name": "Text Highlighter with IndexDB",
  "version": "1.0",
  "permissions": [],
  "content_scripts": [
    {
      "matches": ["<all_urls>"],
      "js": ["content_script.js"],
      "run_at": "document_end"
    }
  ]
}
```

（不再需要 `storage` 权限，因为改用 IndexDB。）

### 说明与注意事项

1. 通过 `db.ts` 封装了 IndexDB 的操作，提供 `saveHighlights` 和 `getHighlights` 两个方法来读写数据。
2. 存储结构为：
    
    ```js
    {
      url: string,
      highlights: HighlightData[]
    }
    ```
    
3. 当用户选中文本时，从IndexDB中取出当前URL的高亮记录数组，将新记录加进去后再存回去。
4. 页面加载时，会从IndexDB中读取对应URL的所有高亮数据，并调用 `restoreHighlight` 来恢复颜色修改。

这样，通过使用IndexDB替代`chrome.storage`，您就可以在本地使用更灵活的数据存储方式来保存和恢复文本区域高亮数据。