'''

@Author: Jayesh Patil
@Date: 2024-08-21
@Last Modified by: Jayesh Patil
@Title: Write a Python program to count the number of characters (character frequency) in a string.
        Sample String : google.com
        Expected Result : {'o': 3, 'g': 2, '.': 1, 'e': 1, 'l': 1, 'm': 1, 'c': 1}
'''
def char_frequency(s):
    """
    Description:
        Counts the frequency of each character in the given string.

    Parameters:
        s (str): The string whose characters' frequency is to be counted.

    Returns:
        dict: A dictionary where the keys are characters and the values are their frequencies.
    """
    frequency_dict = {}
    
    for char in s:
        if char in frequency_dict:
            frequency_dict[char] += 1
        else:
            frequency_dict[char] = 1
    
    return frequency_dict

def main():
    sample_string = "google.com"
    
    result = char_frequency(sample_string)
    
    print("Character frequency in the string '{}':".format(sample_string))
    print(result)

if __name__ == "__main__":
    main()
