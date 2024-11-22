import csv
import os

def create_annotation(save_path: str, annotation_path: str) -> None:
    """
    Creates annotation file with absolute and relative paths of images
    :param save_path: Path to save images
    :param annotation_path: Path to save annotation file
    """
    try:
        with open(annotation_path, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Absolute', 'Relative'])
            for filename in os.listdir(save_path):
                absolute_path = os.path.abspath(os.path.join(save_path, filename))
                relative_path = os.path.relpath(absolute_path, save_path)
                writer.writerow([absolute_path, relative_path])
    except Exception as e:
        raise Exception(f"Cannot create a file: {e}")
