'''

@Author: jayesh Patil
@Date: 2024-08-20
@Last Modified by: Jayesh Patil
@Title : Python program to check whether an element exists within a tuple.

'''
def element_exists(t, element):
    """
    Description :
        Checks whether an element exists within a tuple.

    Parameters:
        t (tuple): The tuple in which to check for the element.
        element: The element to check for in the tuple.

    Returns:
         True if the element exists in the tuple, False otherwise.
    """
    return element in t

def main():
    my_tuple = (10, 20, 30, 40, 50)

    element_to_check = 30

    exists = element_exists(my_tuple, element_to_check)

    if exists:
        print(f"Element {element_to_check} exists in the tuple.")
    else:
        print(f"Element {element_to_check} does not exist in the tuple.")

if __name__ == "__main__":
    main()
