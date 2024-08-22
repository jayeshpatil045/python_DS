'''

@Author: Jayesh Patil
@Date: 2024-08-21
@Last Modified by: Jayesh Patil
@Title: Write a Python program to count occurrences of a substring in a string.
'''
def count_substring(main_string, sub_string):
    """
    Description:
        Counts and returns the number of occurrences of a substring in a main string.

    Parameters:
        main_string (str): The string in which to search for the substring.
        sub_string (str): The substring to count within the main string.

    Returns:
        The number of times the substring occurs in the main string.
    """
    return main_string.count(sub_string)

def main():
    main_string = "Python is an amazing programming language. Python is also popular."
    sub_string = "Python"

    occurrences = count_substring(main_string, sub_string)

    print(f"The substring '{sub_string}' occurs {occurrences} times in the main string.")

if __name__ == "__main__":
    main()
