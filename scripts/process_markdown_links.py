import re
import sys
from pathlib import Path

# 设置要处理的 Markdown 根目录
ORIGIN_PATH = Path("content/chinese/Knowledges/")
OUTPUT_PATH = Path("content/chinese/Knowledges/")

# 正则表达式：匹配 [说明](路径.md)，说明文本可以为空
pattern = re.compile(r'\[([^\]]*)\]\(([^()\s]+?)\.md\)')

def need_skip(file_path: Path):
    return file_path == '_index.md'

def replace_md_links(text: str) -> str:
    def repl(match):
        label = match.group(1)  # 链接说明文本
        path = match.group(2)   # 去掉了 .md 的路径部分
        new_path = f"../{path}"     # 在开头添加 ../
        # 替换空格
        new_path = new_path.strip().replace(" ", "-")
        new_path = new_path.strip().replace("%20", "-")
        return f"[{label}]({new_path})"

    return pattern.sub(repl, text)

if not ORIGIN_PATH.exists():
    print(f'The directory {ORIGIN_PATH} is not exist.')
    sys.exit(0)

# 扫描并修改所有 .md 文件
for md_file in ORIGIN_PATH.rglob("*.md"):
    if need_skip(md_file):
        print(f'Skip {md_file}')
        continue

    original_text = md_file.read_text(encoding="utf-8")
    result_text = replace_md_links(original_text)

    if original_text != result_text:
        md_file.write_text(result_text, encoding="utf-8")
        print(f"✔ 已更新：{md_file}")
