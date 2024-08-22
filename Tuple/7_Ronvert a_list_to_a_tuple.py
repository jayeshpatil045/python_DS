'''

@Author: jayesh Patil
@Date: 2024-08-20
@Last Modified by: Jayesh Patil
@Title : Python program to convert a list to a tuple.

'''
def list_to_tuple(my_list):
    """
    Description :
         Converts a list to a tuple.

    Parameters:
        my_list (list): The list to be converted to a tuple.

    Returns:
         A tuple containing the elements of the list.
    """
    return tuple(my_list)

def main():
    my_list = [1, 2, 3, 4, 5]

    my_tuple = list_to_tuple(my_list)

    print("Converted tuple:", my_tuple)

if __name__ == "__main__":
    main()
