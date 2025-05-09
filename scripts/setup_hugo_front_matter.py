import sys
import datetime
from pathlib import Path

# Run from root directory.

ORIGIN_PATH: Path = Path('origin/chinese/Knowledges')
OUTPUT_PATH: Path = Path('content/chinese/Knowledges')

COVER_IMAGE_PATH: str = 'images/content/'
PRIVATE_DIRECTORY_NAME: str = 'Private'
ORIGIN_KNOWLEDGES_DIRECTORY_NAME: str = 'Knowledges'

def need_skip(file_path: Path):
    path_parts = file_path.parts
    return PRIVATE_DIRECTORY_NAME in path_parts or file_path == '_index.md'

def initialize_yaml(lines: list[str]):
    if lines[0].strip() == '---':
        return

    lines.insert(0, '---\n')
    lines.insert(0, '---\n')

# Todo: Do not mark if there is already a draft configuration.
def mark_as_draft(lines: list[str]):
    if lines[0].strip() != '---':
        return
    
    is_draft = False
    for i in range(1, len(lines)):
        if lines[i].strip() == '---':
            break

        processing_tags = False
        if ':' in lines[i]:
            key, value = lines[i].split(':', 1)
            if key.strip() == 'tags':
                processing_tags = True
            else:
                processing_tags = False

        if processing_tags and lines[i].lower().find('draft') != -1:
            is_draft = True
            break

    if is_draft:
        lines.insert(1, 'draft: true\n')
    else:
        lines.insert(1, 'draft: false\n')

def setup_image(file_path: Path, line: list[str]):
    if lines[0].strip() != '---':
        return
    
    path_parts = file_path.parts
    cover_image_name = 'Default'
    if ORIGIN_KNOWLEDGES_DIRECTORY_NAME in path_parts:
        idx = path_parts.index(ORIGIN_KNOWLEDGES_DIRECTORY_NAME)
        if idx + 1 < len(path_parts):
            cover_image_name = path_parts[idx + 1]
        else:
            print(f'Should use default image for {file_path}.')

    cover_image_file = COVER_IMAGE_PATH + cover_image_name + '.png'
    lines.insert(1, f'image: \"{cover_image_file}\"\n')

def setup_basic_info(file_path: Path, lines: list[str]):
    if lines[0].strip() != '---':
        return
    
    need_title = True
    need_author = True
    need_date = True
    for i in range(1, len(lines)):
        if lines[i].strip() == '---':
            break

        if ':' in lines[i]:
            key, value = lines[i].split(':', 1)
            if key.strip() == 'title':
                need_title = False
            if key.strip() == 'author':
                need_author = False
            if key.strip() == 'date':
                need_date = False

    if need_title:
        lines.insert(1, f'title: \"{file_path.stem}\"\n')
    if need_author:
        lines.insert(2, 'author: \"Roser\"\n')
    if need_date:
        timestamp = datetime.datetime.fromtimestamp(file_path.stat().st_mtime).strftime('%Y-%m-%d')
        lines.insert(3, f'date: {timestamp}\n')

if __name__ == '__main__':
    if not ORIGIN_PATH.exists():
        print(f'The directory {ORIGIN_PATH} is not exist.')
        sys.exit(0)

    if not OUTPUT_PATH.exists():
        OUTPUT_PATH.mkdir(parents=True, exist_ok=True)
        print(f'The directory {OUTPUT_PATH} created.')
        
    for md_file in ORIGIN_PATH.rglob('*.md'):
        lines: list[str] = []

        output_file = OUTPUT_PATH / md_file.relative_to(ORIGIN_PATH)

        if need_skip(md_file):
            print(f'Skip {output_file}.')
            continue

        if output_file.exists():
            print(f'{output_file} exists.')
            continue

        output_file.parent.mkdir(parents=True, exist_ok=True)
        with md_file.open('r', encoding='utf-8') as source_file:
            lines = source_file.readlines()
            
            if len(lines) > 0:
                print(f"Processing {md_file}")

                initialize_yaml(lines)
                mark_as_draft(lines)
                setup_image(md_file, lines)
                setup_basic_info(md_file, lines)

        with output_file.open('w', encoding='utf-8') as target_file:
            target_file.writelines(lines)
