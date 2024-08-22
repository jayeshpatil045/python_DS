'''

@Author: Jayesh Patil
@Date: 2024-08-20
@Last Modified by: Jayesh Patil
@Title: . Write a Python program to sum all the items in a list


'''
def sum_of_list(items):
    """
    Description:

        Calculates and returns the sum of all items in a list.

    Parameters:
        items (list): A list of numbers to sum.

    Returns:
        int/float: The sum of all the numbers in the list.
    """
    return sum(items)

def main():
    my_list = [1, 2, 3, 4, 5]

    total_sum = sum_of_list(my_list)

    print("The sum of all items in the list is:", total_sum)

if __name__ == "__main__":
    main()
