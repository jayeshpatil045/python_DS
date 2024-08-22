'''

@Author: Jayesh Patil
@Date: 2024-08-20
@Last Modified by: Jayesh Patil
@Title: Write a Python program to get the smallest number from a list.


'''
def smallest_number(list1):
    """
    Description:
        Returns the smallest number from a list.

    Parameters:
        items (list): A list of numbers to evaluate.

    Returns:
        The smallest number in the list.
    """
    return min(list1)
def main():
    list1 = [3, 1, 4, 1, 5, 9, 2, 6, 5]
    smallest_num = smallest_number(list1)    
    print(f"smallest number from the list is {smallest_num}")

if __name__ == "__main__":
    main()

