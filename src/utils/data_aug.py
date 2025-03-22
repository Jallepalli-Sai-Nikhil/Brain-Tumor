import tensorflow as tf
import random

def apply_augmentation(img):
    
    # * Covert to tensor (if not already)
    img = tf.convert_to_tensor(img)
    
    # * Randomly flip the image left-right
    img = tf.image.random_flip_left_right(img)
    
    # * Randomly rotate (0, 90, 180, 270 degrees)
    k = random.choice([0, 1, 2, 3])
    img = tf.image.rot90(img, k=k)
    
    # * Randomly adjust brightness
    img = tf.image.random_brightness(img, max_delta=0.2)
    
    # * Randomly adjust contrast
    img = tf.image.random_contrast(img, lower=0.5, upper=1.5)
    
    # * Normalize image
    img = tf.image.per_image_standardization(img)
    
    # * convert to numpy array
    img = img.numpy()
    
    return img
