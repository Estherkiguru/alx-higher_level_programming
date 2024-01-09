#!/usr/bin/python3
"""module for inserting a line of text to a file"""


def append_after(filename="", search_string="", new_string=""):
    """appends new_string"""
    with open(filename, 'r', encoding='utf-8') as file:
        line_list = []
        for lines in file:
            line_list.append(lines)
            if search_string in lines:
                line_list.append(new_string)
    with open(filename, 'w', encoding='utf-8') as file:
        file.writelines(line_list)
