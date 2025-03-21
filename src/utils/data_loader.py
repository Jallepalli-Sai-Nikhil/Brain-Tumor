# utils/data_loader.py

import os
from typing import List, Tuple
from PIL import Image
import numpy as np
from config import Config  # import the config class

def load_images_from_folder(folder_path: str = Config.DATASET_DIR) -> Tuple[np.ndarray, np.ndarray, List[str]]:
    images: List[np.ndarray] = []
    labels: List[int] = []

    # Get sorted class names (folder names)
    class_names: List[str] = sorted(os.listdir(folder_path))

    for label_index, class_name in enumerate(class_names):
        class_folder: str = os.path.join(folder_path, class_name)

        if not os.path.isdir(class_folder):
            continue

        for filename in os.listdir(class_folder):
            if filename.lower().endswith(('.jpg', '.jpeg', '.png')):
                image_path: str = os.path.join(class_folder, filename)

                image: Image.Image = Image.open(image_path).convert('RGB')
                image = image.resize((Config.IMG_WIDTH, Config.IMG_HEIGHT))  # use config
                image_array: np.ndarray = np.array(image, dtype=np.float32) / 255.0

                images.append(image_array)
                labels.append(label_index)

    images_np: np.ndarray = np.array(images)
    labels_np: np.ndarray = np.array(labels)

    return images_np, labels_np, class_names
