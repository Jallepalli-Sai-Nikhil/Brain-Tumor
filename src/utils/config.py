class Config:
    IMAGE_SIZE = (224, 224)
    AUGMENTATION = True
    DATASET_FOLDER = "src/artifacts/dataset"
    ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])
    
    # todo: GCS Settings
    GCS_DEPLOY = False
    GCS_BUCKET_NAME = "gs://your-bucket-name"
    GCS_DATASET_PREFIX = "brain-tumor-dataset"