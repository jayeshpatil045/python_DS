'''

@Author: Jayesh Patil
@Date: 2024-08-20
@Last Modified by: Jayesh Patil
@Title: Write a Python program to find common items from two lists.
'''
def find_common_items_loop(list1, list2):
    """
    Description:
        Finds common items between two lists using a loop.

    Parameters:
        list1 (list): The first list.
        list2 (list): The second list.

    Returns:
         A list of common items.
    """
    common_items = []
    for item in list1:
        if item in list2:
            common_items.append(item)
    return common_items

def main():
    list1 = [1, 2, 3, 4, 5]
    list2 = [4, 5, 6, 7, 8]

    common_items = find_common_items_loop(list1, list2)

    print("Common items (Loop):", common_items)

if __name__ == "__main__":
    main()
