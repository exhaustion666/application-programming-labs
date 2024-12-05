import matplotlib.pyplot as plt
import pandas as pd

def plot_histogram(df: pd.DataFrame) -> None:
    """
    Plot histogram of image area distribution
    :param df: DataFrame with paths, shapes and areas of images
    """
    plt.figure(figsize=(10, 6))
    df['area'].hist(bins=30)
    plt.title('Image area distribution')
    plt.xlabel('Area')
    plt.ylabel('Freq')
    plt.show()
