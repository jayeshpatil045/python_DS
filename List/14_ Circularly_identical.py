'''

@Author: Jayesh Patil
@Date: 2024-08-20
@Last Modified by: Jayesh Patil
@Title: Write a python program to check whether two lists are circularly identical.
'''
def circularly_identical_(list1, list2):
    """
    Description:
        Checks if two lists are circularly identical by rotating one list and comparing.

    Parameters:
        list1 (list): The first list.
        list2 (list): The second list.

    Returns:
         True if the lists are circularly identical, False otherwise.
    """
    if len(list1) != len(list2):
        return False
    
    for i in range(len(list1)):
        if list1[i:] + list1[:i] == list2:
            return True
    
    return False

def main():
    list1 = [1, 2, 3, 4]
    list2 = [3, 4, 1, 2]

    result = circularly_identical_(list1, list2)

    print("Are the two lists circularly identical?", result)

if __name__ == "__main__":
    main()
