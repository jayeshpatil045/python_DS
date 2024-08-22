'''

@Author: Jayesh Patil
@Date: 2024-08-21
@Last Modified by: Jayesh Patil
@Title: Write a Python program to reverse a string.
'''
def reverse_string(string1):
    """
    Description:
        Reverses the input string and returns the reversed string.

    Parameters:
        s (str): The string to be reversed.

    Returns:
        The reversed string.
    """

    return string1[::-1]
def main():
    string1 = input("Enter the string")
    updated_string = reverse_string(string1)
    print(f"string from user{string1} and updated string {updated_string}")

if __name__ == "__main__":
    main()