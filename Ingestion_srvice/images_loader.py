import shutil
from pathlib import Path
import os
from dotenv import load_dotenv
import logging
load_dotenv()


class ImageCopyHandler:
    def __init__(self,logger:logging.Logger):
        self.logger = logger

    def copy_images(self, source_path: Path, project_dir: Path):
        self.logger.info("Copied all images")

        if not project_dir.exists():
            project_dir.mkdir(parents=True, exist_ok=True)

        valid_extensions = ('.png', '.jpg', '.jpeg', '.bmp', '.gif')

        for file in source_path.iterdir():
            if file.is_file() and file.suffix.lower() in valid_extensions:
                shutil.copy2(file, project_dir / file.name)
