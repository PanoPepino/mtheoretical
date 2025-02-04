from pathlib import Path

__all__ = ["split_dictionary_path", "check_file_exists"]


def split_dictionary_path(input_string):
    """This method splits a given string only in the last "/" symbol.

    Args::

        - input_string (str)

    Returns::

        list: ["everything up to the last "/" symbol, "the remaining"]

        - An **Example**::

        split_dictionary_path(the_dictionary) -> ["the path", "the dictionary file"]
    """
    return input_string.rsplit("/", 1)


def check_file_exists(directory, filename):
    """This methods checks if a given file exists in a given directory.

    Args::

        - directory
        - filename

    Returns::

        True or False
    """
    file_path = Path(directory) / filename
    return file_path.is_file()
