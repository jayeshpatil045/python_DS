'''

@Author: Jayesh Patil
@Date: 2024-08-20
@Last Modified by: Jayesh Patil
@Title: Write a Python program to append a list to the second list.
'''

def append_lists(list1, list2):
    """
    Description:
       Appends the elements of the first list to the second list.

    Parameters:
        list1 (list): The list whose elements will be appended.
        list2 (list): The list to which elements will be appended.

    Returns:
        list: The second list after appending elements from the first list.
    """
    list2.extend(list1)
    return list2

def main():
    list1 = [1, 2, 3]
    list2 = ['a', 'b', 'c']

    combined_list = append_lists(list1, list2)

    print("Combined list:", combined_list)

if __name__ == "__main__":
    main()
