#!/usr/bin/python3
"""Prints a text with 2 lines after each of these characters: '.', '?', ':'"""


def text_indentation(text):
    """Print text with two new lines after each '.' '?' ':'

    Parameters:
    text: a string.
    Raises:
    TypeError: if text is not a string.
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    container = []
    i = 0
    length = len(text)

    while i < length:
        if text[i] == '.' or text[i] == ':' or text[i] == '?':
            container.append(text[i])
            if i != length - 1:
                container.append('\n\n')

            i += 1
            while i < length and text[i] == ' ':
                i += 1
            continue
        else:
            container.append(text[i])
        i += 1
    result = ''.join(container)
    print(result, end="")
