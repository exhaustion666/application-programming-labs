import cv2
import numpy as np

def invert_colors(image: np.ndarray) -> np.ndarray:
    """
    Invert colors of the image
    :param image: Source image
    :return: Inverted image
    """
    return cv2.bitwise_not(image)
