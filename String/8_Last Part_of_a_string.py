'''

@Author: Jayesh Patil
@Date: 2024-08-21
@Last Modified by: Jayesh Patil
@Title: Write a Python program to get the last part of a string before a specified character.
        https://www.w3resource.com/python-exercises
        https://www.w3resource.com/python
'''
def get_last_part(input_string, char):
    """
    Description:
        Extracts and returns the last part of the string before the specified character.

    Parameters:
        input_string (str): The input string to be processed.
        char (str): The character before which the last part of the string is extracted.

    Returns:
        The last part of the string before the specified character.
    """
    parts = input_string.split(char)
    
    return char.join(parts[:-1])

def main():
    string1 = "https://www.w3resource.com/python-exercises"
    string2 = "https://www.w3resource.com/python"
    
    char = '/'
    
    result1 = get_last_part(string1, char)
    result2 = get_last_part(string2, char)
    
    print("Original string 1:", string1)
    print("Last part before '{}' in string 1: {}".format(char, result1))
    
    print("Original string 2:", string2)
    print("Last part before '{}' in string 2: {}".format(char, result2))

if __name__ == "__main__":
    main()
