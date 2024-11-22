import cv2
import numpy as np

def load_image(image_path: str) -> np.ndarray:
    """
    Load an image
    :param image_path: Path to the image
    :return: Loaded image as a numpy ndarray
    """
    image = cv2.imread(image_path)
    if image is None:
        raise ValueError(f"Error: Could not read the image from {image_path}")
    return image
