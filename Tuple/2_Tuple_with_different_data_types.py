'''

@Author: jayesh Patil
@Date: 2024-08-20
@Last Modified by: Jayesh Patil
@Title : Python program to create a tuple with different data types.

'''
def create_tuple():
    """
    Description :
        Creates and returns a tuple containing elements of different data types.

    Returns:
        tuple: A tuple containing an integer, a string, a float, a list, and a dictionary.
    """
    mixed_tuple = (42, "Hello, World!", 3.14159, [1, 2, 3], {"key": "value"})
    return mixed_tuple

def main():
    result_tuple = create_tuple()

    print("Created tuple with different data types:", result_tuple)

if __name__ == "__main__":
    main()
