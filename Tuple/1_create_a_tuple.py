'''

@Author: jayesh Patil
@Date: 2024-08-20
@Last Modified by: Jayesh Patil
@Title : Write a Python program to create a tuple.

'''
def create_tuple():
    """
    Description :
        Creates and returns a tuple with different types of elements.

    Returns:
         A tuple containing integers, strings, and a list.
    """
    my_tuple = (1, "Hello", 3.14, [5, 6, 7])
    return my_tuple

def main():
    # Create a tuple
    result_tuple = create_tuple()

    # Print the created tuple
    print("Created tuple:", result_tuple)

if __name__ == "__main__":
    main()
