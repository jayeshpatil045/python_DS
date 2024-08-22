'''

@Author: Jayesh Patil
@Date: 2024-08-21
@Last Modified by: Jayesh Patil
@Title:  Write a Python function that takes a list of words and returns the length of the longest one.
'''
def longest_word_length(words):
    """
    Description:
        Finds and returns the length of the longest word in a given list of words.

    Parameters:
        words (list): A list of words (strings).

    Returns:
        The length of the longest word in the list. If the list is empty, returns 0.
    """
    if not words:  
        return 0
    
    max_length = max(len(word) for word in words)  
    return max_length

def main():
    words_list = ["apple", "banana", "cherry", "blueberry", "strawberry"]
    
    longest_length = longest_word_length(words_list)
    
    print("List of words:", words_list)
    print("Length of the longest word:", longest_length)

if __name__ == "__main__":
    main()
