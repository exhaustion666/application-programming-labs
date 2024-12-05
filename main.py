from df import add_image_shape, compute_area, create_df, get_statistics, filter_images
from histogram import plot_histogram
from parse_args import parse_args

def main():
    try:
        annotation_path, max_width, max_height = parse_args()
        df = create_df(annotation_path)
        add_image_shape(df)
        print("Statistics:\n", get_statistics(df))
        print("DataFrame:\n", df)
        filtered_df = filter_images(df, max_width, max_height)
        print("Filtered DataFrame:\n", filtered_df)
        df_sorted = compute_area(df).sort_values(by='area')
        print("Filtered DataFrame by area:\n", df_sorted)
        plot_histogram(df)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
    