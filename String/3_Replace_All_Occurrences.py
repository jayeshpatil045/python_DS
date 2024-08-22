'''

@Author: Jayesh Patil
@Date: 2024-08-21
@Last Modified by: Jayesh Patil
@Title: Write a Python program to get a string from a given string where all occurrences of its
        first char have been changed to '$', except the first char itself.
        Sample String : 'restart'
        Expected Result : 'resta$t'
'''
def replace_char(s):
    """
    Description:
        Replaces all occurrences of the first character in the string with '$', except for the first occurrence.

    Parameters:
        s (str): The string in which to perform the replacement.

    Returns:
        The modified string with all occurrences of the first character replaced by '$', except the first occurrence.
    """
    first_char = s[0]  
    modified_string = first_char + s[1:].replace(first_char, '$')
    return modified_string

def main():
    sample_string = "restart"
    
    result = replace_char(sample_string)
    
    print("Original String:", sample_string)
    print("Modified String:", result)

if __name__ == "__main__":
    main()
