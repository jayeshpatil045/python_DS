'''

@Author: jayesh Patil
@Date: 2024-08-20
@Last Modified by: Jayesh Patil
@Title : Creates and returns a clone of the given tuple.

'''
from collections import Counter

def find_repeated_items(t):
    """
    Description :
        Finds and returns the repeated items in a tuple.

    Parameters:
        t (tuple): The tuple to check for repeated items.

    Returns:
        A list of repeated items in the tuple.
    """
    element_count = Counter(t)
    
    repeated_items = [item for item, count in element_count.items() if count > 1]
    
    return repeated_items

def main():
    my_tuple = (1, 2, 3, 2, 4, 5, 6, 3, 2,6)

    repeated_items = find_repeated_items(my_tuple)

    print("Repeated items in the tuple:", repeated_items)

if __name__ == "__main__":
    main()
