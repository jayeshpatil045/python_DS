'''

@Author: Jayesh Patil
@Date: 2024-08-20
@Last Modified by: Jayesh Patil
@Title: Write a Python program to clone or copy a list.
'''
def clone_list_using_copy(original_list):
    """
    Description:
        Clones or copies a list using the copy() method.

    Parameters:
        original_list (list): The list to be cloned.

    Returns:
        A new list that is a copy of the original list.
    """
    return original_list.copy()

def main():
    sample_list = [1, 2, 3, 4, 5]

    cloned_list = clone_list_using_copy(sample_list)

    print("Original List:", sample_list)
    print("Cloned List:", cloned_list)

if __name__ == "__main__":
    main()
