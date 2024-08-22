'''

@Author: jayesh Patil
@Date: 2024-08-19
@Last Modified by: Jayesh Patil
@Title : Write a Python program to iteration over sets.
'''

def iterate_over_set(my_set):
    """
    Description :
        Iterates over the elements of a set and prints each element.

    Parameters:
        my_set (set): The set to iterate over.
    """
    for item in my_set:
        print(item)

def main():
    # Sample set
    sample_set = {10, 20, 30, 40, 50}
    
    # Iterate over the set and print each element
    print("Iterating over the set:")
    iterate_over_set(sample_set)

if __name__ == "__main__":
    main()
