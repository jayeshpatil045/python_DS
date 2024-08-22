'''

@Author: Jayesh Patil
@Date: 2024-08-20
@Last Modified by: Jayesh Patil
@Title: Write a Python program to get the difference between the two lists.
'''
def list_difference_set(list1, list2):
    """
    Description:
        Computes the difference between two lists using sets.

    Parameters:
        list1 (list): The first list.
        list2 (list): The second list to subtract from the first list.

    Returns:
         A list containing elements that are in list1 but not in list2.
    """
    return list(set(list1) - set(list2))

def main():
    list1 = [1, 2, 3, 4, 5]
    list2 = [3, 4, 5, 6, 7]

    difference = list_difference_set(list1, list2)

    print("Difference between list1 and list2 using sets:", difference)

if __name__ == "__main__":
    main()
