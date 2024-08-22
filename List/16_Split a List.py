'''

@Author: Jayesh Patil
@Date: 2024-08-20
@Last Modified by: Jayesh Patil
@Title: Write a Python program to split a list based on first character of word.
'''
from collections import defaultdict

def split_list_by_first_char(word_list):
    """
    Description:
       Splits a list of words into a dictionary based on the first character of each word.

    Parameters:
        word_list (list): A list of words to be split.

    Returns:
        A dictionary where each key is a first character, and the value is a list of words starting with that character.
    """
    split_dict = defaultdict(list)
    
    for word in word_list:
        first_char = word[0]
        split_dict[first_char].append(word)
    
    return dict(split_dict)

def main():
    word_list = ['apple', 'banana', 'cherry', 'apricot', 'blueberry', 'avocado', 'cranberry']

    result = split_list_by_first_char(word_list)

    print("List split based on the first character of each word:")
    for char, words in result.items():
        print(f"{char}: {words}")

if __name__ == "__main__":
    main()
