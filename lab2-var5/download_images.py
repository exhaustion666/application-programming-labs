import os
from icrawler.builtin import GoogleImageCrawler

def download_images(keyword: str, save_path: str, count: int) -> None:
    """
    Uploads images by keyword
    :param keyword: Word for search
    :param save_path: Path to save images
    :param count: Count of images to download
    """
    try:
        google_crawler = GoogleImageCrawler(storage={'root_dir': save_path})
        google_crawler.crawl(keyword=keyword, max_num=count)
    except Exception as e:
        raise Exception(f"Error loading images: {e}")
