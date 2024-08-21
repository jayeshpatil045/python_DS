'''

@Author: Jayesh Patil
@Date: 2024-08-20
@Last Modified by: Jayesh Patil
@Title: Write a Python program to remove duplicates from a list

'''
def remove_duplicate(list1):
    """
    Description:
              Removes duplicates from a list and returns a list of unique items.

    Parameters:
              items (list): A list of elements that may contain duplicates.

    Returns:
              A list containing only the unique elements from the original list.
    """
    return set(list1)
def main():
    list1 = [1, 2, 3, 2, 4, 5, 1, 6, 3, 4]
    unique_list = remove_duplicate(list1)
    print("the unique list is ",unique_list)
if __name__ == "__main__":
    main()    
