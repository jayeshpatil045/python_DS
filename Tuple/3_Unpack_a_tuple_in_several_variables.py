'''

@Author: jayesh Patil
@Date: 2024-08-20
@Last Modified by: Jayesh Patil
@Title :Python program to unpack a tuple in several variables.

'''
def unpack_tuple(t):
    """
    Description :
        Unpacks a tuple into individual variables and prints them.

    Parameters:
        t (tuple): The tuple to be unpacked.

    Returns:
        None
    """
    a, b, c, d, e = t
    print("Value of a:", a)
    print("Value of b:", b)
    print("Value of c:", c)
    print("Value of d:", d)
    print("Value of e:", e)

def main():
    my_tuple = (42, "Hello", 3.14, [1, 2, 3], {"key": "value"})

    unpack_tuple(my_tuple)

if __name__ == "__main__":
    main()
