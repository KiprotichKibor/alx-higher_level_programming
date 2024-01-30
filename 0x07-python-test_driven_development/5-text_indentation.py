#!/usr/bin/python3
def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters: . , ? and :

    Parameters:
    text (str): The input text.

    Raises:
    TypeError: If text is not a string.
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")
    """check if text is a string"""

    result = ""
    """initialize an empty result string"""

    for char in text:
        """iterate through each character in the text"""
        result += char
        """append the character to the result string"""
        if char in (".", "?", ":"):
            """if the character is .,? or : add two new lines to the result string"""
            result += "\n\n"

    print(result)
    """print the result string"""
