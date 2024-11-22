import argparse

def parse_args():
    """
    Parsing command line arguments
    :return: Command line arguments
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('input_image', type=str, help="Path to the input image")
    parser.add_argument('output_image', type=str, help="Path to save the output image")
    args = parser.parse_args()
    return args.input_image, args.output_image
