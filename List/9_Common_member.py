'''

@Author: Jayesh Patil
@Date: 2024-08-20
@Last Modified by: Jayesh Patil
@Title: Write a Python function that takes two lists and returns True if they have at
        least one common member.
'''
def find_long_words(words, n):
    """
    Description: Finds and returns a list of words that are longer than a given length.

    Parameters:
        words (list): A list of words to search through.
        n (int): The minimum length of the words to be included in the result.

    Returns:
        A list of words that are longer than the specified length.
    """
    return [word for word in words if len(word) > n]

def main():
    sample_words = ["hello", "world", "Python", "programming", "is", "awesome"]

    n = 5

    long_words = find_long_words(sample_words, n)

    print(f"Words longer than {n} characters:", long_words)

if __name__ == "__main__":
    main()
