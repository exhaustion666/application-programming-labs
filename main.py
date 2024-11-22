import cv2
import numpy as np

from display_image import display_image, plot_histogram
from invert_colors import invert_colors
from load_image import load_image
from parse_agrs import parse_args

def main():
    input_image_path, output_image_path = parse_args()
    image = load_image(input_image_path)
    print(f"Image size: {image.shape[1]} x {image.shape[0]} (Width x Height)")
    plot_histogram(image)
    inverted_image = invert_colors(image)
    display_image(image, title='Original Image')
    display_image(inverted_image, title='Inverted Image')
    try:
        cv2.imwrite(output_image_path, inverted_image)
        print(f"Inverted image saved to {output_image_path}")
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()
