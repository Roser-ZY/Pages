import sys
import shutil
from pathlib import Path

# Run from root directory.

ORIGIN_PATH: Path = Path('origin/chinese/Knowledges')
OUTPUT_PATH: Path = Path('assets/images')

IMAGE_DIRECTORY_NAME: str = 'images'

if not ORIGIN_PATH.exists():
    print(f'The directory {ORIGIN_PATH} is not exist.')
    sys.exit(0)

if not OUTPUT_PATH.exists():
    OUTPUT_PATH.mkdir(parents=True, exist_ok=True)
    print(f'The directory {OUTPUT_PATH} created.')

for image_dir in ORIGIN_PATH.rglob('*'):
    if image_dir.is_dir() and image_dir.name.lower() == IMAGE_DIRECTORY_NAME:
        for image_file in image_dir.iterdir():
            output_file = OUTPUT_PATH / image_file.name
            if not output_file.exists():
                shutil.copy2(image_file, output_file)
                print(f'Copy {image_file} to {output_file}.')

