'''

@Author: Jayesh Patil
@Date: 2024-08-20
@Last Modified by: Jayesh Patil
@Title: Write a Python program to remove duplicates from a list of lists.
        Sample list : [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
        New List : [[10, 20], [30, 56, 25], [33], [40]]
'''
def remove_duplicates(list_of_lists):
    """
    Des
    cription:
       Removes duplicate lists from a list of lists while preserving the original order.

    Parameters:
        list_of_lists (list): A list containing other lists.

    Returns:
        A new list with duplicates removed, preserving order.
    """
    unique_lists = []
    seen = set()
    
    for lst in list_of_lists:
        t = tuple(lst)
        if t not in seen:
            seen.add(t)
            unique_lists.append(lst)
    
    return unique_lists

def main():
    list_of_lists = [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
    
    new_list = remove_duplicates(list_of_lists)
    
    print("Original List:", list_of_lists)
    print("New List after removing duplicates (preserving order):", new_list)

if __name__ == "__main__":
    main()
