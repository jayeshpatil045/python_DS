'''

@Author: jayesh Patil
@Date: 2024-08-16
@Last Modified by: Jayesh Patil
@Title : Reverse the Order of Items in an Array in Python


'''
from array import array

def reverse_array(arr):
    """
    Reverses the elements of an array.

    Parameters:
        arr (list): A list of integers to be reversed.

    Returns:
        list: The reversed list of integers.
    """
    arr.reverse()
    return arr

def main():
    """
    Creates an integer array, reverses its elements, and prints the reversed array.
    """
    
    int_array = [12, 34, 45, 56, 78]
    
    
    reversed_array = reverse_array(int_array)
    
   
    print(reversed_array)


if __name__ == "__main__":
    main()
