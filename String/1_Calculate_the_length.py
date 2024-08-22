'''

@Author: Jayesh Patil
@Date: 2024-08-21
@Last Modified by: Jayesh Patil
@Title: Write a Python program to calculate the length of a string.
'''
def string_length(s):
    """
    Description:
        Calculates the length of a given string.

    Parameters:
        s (str): The string whose length is to be calculated.

    Returns:
        int: The length of the string.
    """
    return len(s)

def main():
    sample_string = "Hello, World!"
    
    length = string_length(sample_string)
    
    print(f"The length of the string '{sample_string}' is: {length}")

if __name__ == "__main__":
    main()
