#!/usr/bin/python3
"""Defines a text file insertion function."""


def append_after(filename="", search_string="", new_string=""):
    """Insert text after each line containing a given string in a file.

    Args:
        filename (str): The name of the file.
        search_string (str): The string to search for within the file.
        new_string (str): The string to insert.
    """
    updated_content = ""
    with open(filename) as file_reader:
        for line in file_reader:
            updated_content += line
            if search_string in line:
                updated_content += new_string
    with open(filename, "w") as file_writer:
        file_writer.write(updated_content)
