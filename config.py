# config.py

import os
from typing import ClassVar

class Config:
    # Root directory of the project
    BASE_DIR: ClassVar[str] = os.path.dirname(os.path.abspath(__file__))

    # Dataset folder path (you can change 'dataset_folder' to your actual folder name)
    DATASET_DIR: ClassVar[str] = os.path.join(BASE_DIR, "..", "dataset_folder")

    # Image size config (use this for consistency)
    IMG_HEIGHT: ClassVar[int] = 224
    IMG_WIDTH: ClassVar[int] = 224

    # You can add more config here later (models dir, logs, etc.)
