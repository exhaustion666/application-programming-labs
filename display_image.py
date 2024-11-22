import cv2
import matplotlib.pyplot as plt
import numpy as np

def display_image(image: np.ndarray, title: str = 'Image') -> None:
    """
    Display an image
    :param image: Source image
    :param title: Title of the image
    """
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.title(title)
    plt.axis('off')
    plt.show()

def plot_histogram(image: np.ndarray) -> None:
    """
    Plot histogram of source image
    :param image: Source image
    """
    colors = ('b', 'g', 'r')
    plt.figure()
    for i, color in enumerate(colors):
        hist = cv2.calcHist([image], [i], None, [256], [0, 256])
        plt.plot(hist, color=color)
        plt.xlim([0, 256])
    plt.title('Histogram')
    plt.xlabel('Pixel Value')
    plt.ylabel('Frequency')
    plt.show()
