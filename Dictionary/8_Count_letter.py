'''
@Author: jayesh Patil
@Date: 2024-08-19
@Last Modified by: Jayesh Patil
@Title :  Write a Python program to count letter.

'''
def count_letters(input_string):
    """
Description:

    The `count_letters` function counts the frequency of each letter in a given string.
   
Parameters:

    input_string (str):
        - The string whose letters you want to count.
        - This string is passed into the function and is processed character by character.

Returns:

    dict:
        - The function returns a dictionary where the keys are the letters from the input string and the values are the counts of how many times each letter appears.
"""


    letter_count = {}
    for letter in input_string:
        if letter in letter_count:
            letter_count[letter] += 1
        else:
            letter_count[letter] = 1
    return letter_count

def main():
   
    sample_string = 'w3resource'
    
    output_dict = count_letters(sample_string)
    
    print(output_dict)

if __name__ == "__main__":
    main()
