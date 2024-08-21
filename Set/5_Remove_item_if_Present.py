'''

@Author: jayesh Patil
@Date: 2024-08-19
@Last Modified by: Jayesh Patil
@Title : program to remove an item from a set if it is present in the set.

'''
def remove_item_if_present(my_set, item):
    """
    Description :
        Removes an item from the set if it is present.

    Parameters:
        my_set (set): The set from which the item will be removed.
        item: The item to remove from the set.

    Returns:
        set: The set after the item has been removed (if it was present).
    """
    my_set.discard(item)
    return my_set

def main():
    # Sample set
    sample_set = {10, 20, 30, 40, 50}
    
    # Item to remove
    item_to_remove = 30
    
    # Remove the item if it is present
    updated_set = remove_item_if_present(sample_set, item_to_remove)
    
    # Print the updated set
    print("Set after attempting to remove the item:", updated_set)

if __name__ == "__main__":
    main()
