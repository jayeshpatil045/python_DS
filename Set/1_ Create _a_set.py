'''

@Author: jayesh Patil
@Date: 2024-08-19
@Last Modified by: Jayesh Patil
@Title :Write a Python program to create a set. 


'''
def create_set_with_function():
    """
    Description:
    Creates and returns a set using the set() function.
    Parametrs :
    The function initializes a set with a list of integers [1, 2, 3, 4, 5]. 
    Sets are collections of unique, unordered elements.

    Returns:
        set: A set containing the elements {1, 2, 3, 4, 5}.
    """
    my_set = set([1, 2, 3, 4, 5])
    return my_set

def main():
    result_set = create_set_with_function()
    print("Set created using set() function:", result_set)

if __name__ == "__main__":
    main()
