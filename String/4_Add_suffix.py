'''

@Author: Jayesh Patil
@Date: 2024-08-21
@Last Modified by: Jayesh Patil
@Title: Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If the given string already ends with 'ing' then add 'ly' instead. If the string length of the
        given string is less than 3, leave it unchanged.
        Sample String : 'abc'
        Expected Result : 'abcing'
        Sample String : 'string'
        Expected Result : 'stringly'
'''
def add_suffix(s):
    """
    Description:
        Adds 'ing' at the end of the given string if it is at least 3 characters long.
        If the string already ends with 'ing', adds 'ly' instead.
        If the string length is less than 3, leaves it unchanged.

    Parameters:
        s (str): The string to modify.

    Returns:
        The modified string.
    """
    if len(s) >= 3:
        if s.endswith('ing'):
            return s + 'ly'
        else:
            return s + 'ing'
    else:
        return s

def main():
    sample_string1 = "abc"
    sample_string2 = "string"
    sample_string3 = "go"
    
    result1 = add_suffix(sample_string1)
    result2 = add_suffix(sample_string2)
    result3 = add_suffix(sample_string3)
    
    print("Original String:", sample_string1)
    print("Modified String:", result1)
    
    print("Original String:", sample_string2)
    print("Modified String:", result2)
    
    print("Original String:", sample_string3)
    print("Modified String:", result3)

if __name__ == "__main__":
    main()
