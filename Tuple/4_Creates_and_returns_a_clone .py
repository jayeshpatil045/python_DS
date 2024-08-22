'''

@Author: jayesh Patil
@Date: 2024-08-20
@Last Modified by: Jayesh Patil
@Title : Creates and returns a clone of the given tuple.

'''
def clone_tuple(original_tuple):
    """
    Description :
        Creates and returns a clone of the given tuple.

    Parameters:
        original_tuple (tuple): The tuple to be cloned.

    Returns:
        A new tuple that is a clone of the original tuple.
    """
    cloned_tuple = original_tuple[:]  
    return cloned_tuple

def main():
    my_tuple = (1, 2, 3, 4, 5)

    cloned_tuple = clone_tuple(my_tuple)

    print("Original tuple:", my_tuple)
    print("Cloned tuple:", cloned_tuple)

if __name__ == "__main__":
    main()
