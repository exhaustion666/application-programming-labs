import argparse

def parse_args():
    """
    Parsing command line arguments
    :return: Command line arguments
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('keyword', type=str, help="Word for search")
    parser.add_argument('count', type=int, help="Count of images to download")
    parser.add_argument("save_path", type=str, help="Path to save images")
    parser.add_argument("annotation_path", type=str, help="Path to save annotation file")
    args = parser.parse_args()
    return args.keyword, args.count, args.save_path, args.annotation_path
