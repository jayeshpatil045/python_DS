'''

@Author: Jayesh Patil
@Date: 2024-08-21
@Last Modified by: Jayesh Patil
@Title: Write a Python program to lowercase first n characters in a string def lowercase_first_n(s, n):
'''
def lowercase_first_n(s, n):
    """
    Description:
        Lowercases the first n characters of the input string.

    Parameters:
        s (str): The input string.
        n (int): The number of characters to convert to lowercase.

    Returns:
        The string with the first n characters lowercased.
    """
    result = ""

    for i in range(len(s)):
        if i < n:
            result += s[i].lower()
        else:
            result += s[i]
    
    return result

def main():
    original_string = "PYTHON Programming"
    
    n = 6

    modified_string = lowercase_first_n(original_string, n)

    print(f"Original string: {original_string}")
    print(f"Modified string: {modified_string}")

if __name__ == "__main__":
    main()
