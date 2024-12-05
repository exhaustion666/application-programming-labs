import cv2
import os
import pandas as pd 

def add_image_shape(df : pd.DataFrame) -> pd.DataFrame:
    """
    Adds shapes of images in DataFrame 
    :param df: DataFrame with 2 columns
    :return: DataFrame with paths and shapes of images
    """
    height, width, depth = [],[],[]
    for Absolute in df["Absolute"]:
        img = cv2.imread(Absolute)
        if os.path.isfile(Absolute) and img is not None:
            hwd = img.shape
            height.append(hwd[0])
            width.append(hwd[1])
            depth.append(hwd[2])
        else:
            raise FileNotFoundError
    df["height"] = height
    df["width"] = width
    df["depth"] = depth
    return df


def compute_area(df: pd.DataFrame) -> pd.DataFrame:
    """
    Computes the area of image and adds in column
    :param df: DataFrame with paths and shapes of images
    :return: DataFrame with paths, shapes and areas of images
    """
    df['area'] = df['height'] * df['width']
    return df


def create_df(annotation_path : str) -> pd.DataFrame:
    """
    Creates DataFrame with 2 columns
    :param annotation_path: Path to annotation file
    :return: DataFrame with 2 columns
    """
    if os.path.isfile(annotation_path):
        df = pd.read_csv(annotation_path)
        return df
    else:
        raise FileNotFoundError


def get_statistics(df: pd.DataFrame) -> pd.DataFrame:
    """
    Сalculates statistics for columns containing information about image dimensions.
    :param df: DataFrame  with paths and shapes of images
    :return: DataFrame statistics with information about image dimensions.
    """
    return df[['height', 'width', 'depth']].describe()


def filter_images(df: pd.DataFrame, max_width: int, max_height: int) -> pd.DataFrame:
    """
    Filters DataFrame by the specified parameters
    :param df: DataFrame with paths and shapes of images
    :param max_width: Maximum width of filtering
    :param max_height: Maximum height of filtering
    :return: Filtered DataFrame by the specified parameters
    """
    return df[(df['height'] <= max_height) & (df['width'] <= max_width)]
