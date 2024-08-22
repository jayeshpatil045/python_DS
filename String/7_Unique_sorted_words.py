'''

@Author: Jayesh Patil
@Date: 2024-08-21
@Last Modified by: Jayesh Patil
@Title: Write a Python program that accepts a comma separated sequence of words as input and prints the unique words in sorted form (alphanumerically).
        Sample Words : red, white, black, red, green, black
        Expected Result : black, green, red, white,red
'''
def unique_sorted_words(input_string):
    """
    Description:
        Takes a comma-separated string of words, removes duplicates, and sorts them alphanumerically.

    Parameters:
        input_string (str): A comma-separated string of words.

    Returns:
        A sorted list of unique words.
    """
    words = input_string.split(",")
    
    unique_words = set(word.strip() for word in words)
    
    sorted_words = sorted(unique_words)
    
    return sorted_words

def main():

    user_input = input("Enter a comma-separated sequence of words: ")
    
    sorted_unique_words = get_unique_sorted_words(user_input)
    
    print("Sorted unique words:", ", ".join(sorted_unique_words))

if __name__ == "__main__":
    main()
