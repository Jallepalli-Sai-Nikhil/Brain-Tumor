import os
import numpy as np
from PIL import Image
from src.utils.data_aug import apply_augmentation
from src.utils.config import Config

from io import BytesIO

# * If GCS_DEPLOY is True, import Google Cloud Storage
if Config.GCS_DEPLOY == True:
    from google.cloud import storage
    
# * =================================================================
# * CONSTANTS
# * =================================================================

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

# * -------------------------------------------------------------------
# * HELPER FUNCTIONS
# * -------------------------------------------------------------------

def is_image_file(filename):
    return filename.lower().endswith(tuple(ALLOWED_EXTENSIONS))

# * -------------------------------------------------------------------
# * MAIN DATA LOADER FUNCTION
# * -------------------------------------------------------------------

def load_dataset(data_dir=Config.DATASET_FOLDER,
                 image_size=Config.IMAGE_SIZE,
                 augment=Config.AUGMENTATION):
    
    if Config.GCS_DEPLOY == True:
        print(f"[INFO] Loading dataset from GCS...")
        return load_dataset_from_gcs(data_dir, image_size, augment)
    else:
        print(f"[INFO] Loading dataset from local directory...")
        return load_dataset_from_local(data_dir, image_size, augment)
    
# * -------------------------------------------------------------------
# * LOCAL DATA LOADER FUNCTION
# * -------------------------------------------------------------------

def load_dataset_from_local(data_dir, image_size, augment):
    
    images = []
    labels = []
    
    class_names = sorted(os.listdir(data_dir))
    num_classes = len(class_names)
    class_to_idx = {class_name: idx for idx, class_name in enumerate(class_names)}
    
    print(f"[INFO] Found {num_classes} classes Locally...")
    
    # * Iteratie through each class
    
    for class_name in class_names:
        class_folder = os.path.join(data_dir, class_name)
        
        if not os.path.isdir(class_folder):
            continue
        
        # * Iterate through each image in class folder
        for filename in os.listdir(class_folder):
            if not is_image_file(filename):
                continue
            
            file_path = os.path.join(class_folder, filename)
            
        try:
            img = Image.open(file_path).convert('RGB')
            img = img.resize(image_size)
            
            if augment:
                img = apply_augmentation(img)
                
            img_array = np.array(img)/255.0
            images.append(img_array)
            labels.append(class_to_idx[class_name])
            
        except Exception as e:
            print(f"[ERROR] Error loading image {filename}: {str(e)}")
            
    print(f"[INFO] Loaded {len(images)} images Locally...")
    return np.array(images), np.array(labels), class_to_idx

# * -------------------------------------------------------------------
# * GCS DATA LOADER FUNCTION
# * -------------------------------------------------------------------

def load_dataset_from_gcs(data_dir, image_size, augment):
    
    images = []
    labels = []

    # Initialize GCS Client
    storage_client = storage.Client()
    bucket = storage_client.bucket(Config.GCS_BUCKET_NAME)

    # Collect blobs (files) under the given prefix
    blobs = list(storage_client.list_blobs(bucket, prefix=Config.GCS_DATASET_PREFIX))

    if not blobs:
        print("[ERROR] No files found in GCS with the given prefix.")
        return np.array(images), np.array(labels), {}

    # Extract class names from folder names
    class_names_set = set()
    for blob in blobs:
        parts = blob.name.split('/')
        if len(parts) >= 2 and parts[-1]:  # Ignore empty file names (folders)
            class_names_set.add(parts[-2])

    class_names = sorted(class_names_set)
    class_to_idx = {class_name: idx for idx, class_name in enumerate(class_names)}

    print(f"[INFO] Classes found in GCS: {class_to_idx}")

    # Iterate through blobs and process images
    for blob in blobs:
        filename = blob.name
        parts = filename.split('/')

        if len(parts) < 2 or not parts[-1]:
            continue  # Skip directories or incomplete paths

        class_name = parts[-2]

        if class_name not in class_to_idx or not is_image_file(filename):
            continue

        try:
            # Download blob content as bytes
            img_bytes = blob.download_as_bytes()

            # Load image from bytes without saving locally
            img = Image.open(BytesIO(img_bytes)).convert('RGB')
            img = img.resize(image_size)

            if augment:
                img = apply_augmentation(img)

            img_array = np.array(img) / 255.0
            images.append(img_array)
            labels.append(class_to_idx[class_name])

        except Exception as e:
            print(f"[ERROR] Error loading image {filename} from GCS: {e}")

    print(f"[INFO] Loaded {len(images)} images from GCS.")
    return np.array(images), np.array(labels), class_to_idx