'''

@Author: jayesh Patil
@Date: 2024-08-19
@Last Modified by: Jayesh Patil
@Title : Write a Python program to clear a set.

'''
def clear_set(my_set):
    """
    Description :
       Clears all elements from the set.

    Parameters:
        my_set (set): The set to be cleared.

    Returns:
        set: The cleared (empty) set.
    """
    my_set.clear()
    return my_set

def main():
    sample_set = {1, 2, 3, 4, 5}
    
    print("Original set:", sample_set)
    
    cleared_set = clear_set(sample_set)
    
    print("Cleared set:", cleared_set)

if __name__ == "__main__":
    main()
