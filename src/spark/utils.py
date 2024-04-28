from pyspark.sql import DataFrame


def count_lines(text_df: DataFrame, param: str) -> int:
    """Count lines in DataFrame that contain a given string.

    Examples:
    >>> count_lines(text_df, "a")
    2

    :param text_df:
    :param param:
    :return:
    """
    return text_df.filter(text_df.value.contains(param)).count()
