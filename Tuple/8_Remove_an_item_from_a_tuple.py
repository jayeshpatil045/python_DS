'''
@Author: jayesh Patil
@Date: 2024-08-20
@Last Modified by: Jayesh Patil
@Title : Python program to remove an item from a tuple

'''
def remove_item_from_tuple(t, item):
    """
    Description :
        Removes an item from a tuple and returns a new tuple.

    Parameters:
        t (tuple): The original tuple.
        item: The item to be removed from the tuple.

    Returns:
        tuple: A new tuple with the specified item removed.
    """
    temp_list = list(t)
    
    if item in temp_list:
        temp_list.remove(item)
    
    new_tuple = tuple(temp_list)
    
    return new_tuple

def main():
    my_tuple = (1, 2, 3, 4, 5)
    
    item_to_remove = 3
    
    updated_tuple = remove_item_from_tuple(my_tuple, item_to_remove)
    
    print("Original tuple:", my_tuple)
    print("Updated tuple:", updated_tuple)

if __name__ == "__main__":
    main()
