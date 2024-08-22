'''
@Author: jayesh Patil
@Date: 2024-08-20
@Last Modified by: Jayesh Patil
@Title :  Python program to reverse a tuple.

'''
def reverse_tuple(t):
    """
    Description :
        Reverses a tuple.

    Parameters:
        t (tuple): The tuple to be reversed.

    Returns:
        tuple: A new tuple that is the reverse of the original tuple.
    """
    return t[::-1]

def main():
    my_tuple = (10, 20, 30, 40, 50)

    reversed_tuple = reverse_tuple(my_tuple)

    print("Original tuple:", my_tuple)
    print("Reversed tuple:", reversed_tuple)

if __name__ == "__main__":
    main()
