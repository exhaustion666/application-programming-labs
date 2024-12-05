import argparse

def parse_args():
    """
    Parsing command line arguments
    :return: Command line arguments
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("annotation_path", type=str, help="Path to annotation file")
    parser.add_argument('max_width', type=int, help="Maximum width of image")
    parser.add_argument('max_height', type=int, help="Maximum height of image")
    args = parser.parse_args()
    return args.annotation_path, args.max_width, args.max_height
