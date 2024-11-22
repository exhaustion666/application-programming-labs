from create_annotation import create_annotation
from download_images import download_images
from iterator import SimpleIterator
from parse_args import parse_args

def main():
    keyword, count, save_path, annotation_path = parse_args()
    try:
        download_images(keyword, save_path, count)
        create_annotation(save_path, annotation_path)
        iterator = SimpleIterator(annotation_path=annotation_path)
        for image in iterator:
            print(image)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
