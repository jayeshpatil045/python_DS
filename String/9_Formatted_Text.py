'''

@Author: Jayesh Patil
@Date: 2024-08-21
@Last Modified by: Jayesh Patil
@Title:Write a Python program to display formatted text (width=50) as output.
'''
import textwrap

def format_text(input_text, width=50):
    """
    Description:
        Formats the input text to fit within a specified width.

    Parameters:
        input_text (str): The text to be formatted.
        width (int): The maximum width of each line. Default is 50.

    Returns:
        The formatted text with line breaks inserted to fit the specified width.
    """
    return textwrap.fill(input_text, width=width)

def main():
    sample_text = ("Python is an interpreted high-level general-purpose programming language. "
                   "Its design philosophy emphasizes code readability with the use of significant indentation.")

    width = 50

    formatted_text = format_text(sample_text, width)

    print(formatted_text)

if __name__ == "__main__":
    main()
