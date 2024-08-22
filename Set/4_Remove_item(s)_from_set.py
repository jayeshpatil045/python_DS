'''

@Author: jayesh Patil
@Date: 2024-08-19
@Last Modified by: Jayesh Patil
@Title :  Python program to remove item(s) from set.

'''
def remove_single_item(my_set, item):
    """
    Description :
        Removes a single item from the set.

    Parameters:
        my_set (set): The set from which the item will be removed.
        item: The item to remove from the set.

    Returns:
        set: The set after the item has been removed.
    """
    try:
        my_set.remove(item)
    except KeyError:
        print(f"Item '{item}' not found in the set.")
    return my_set

def main():
    # Sample set
    sample_set = {1, 2, 3, 4, 5}
    
    # Remove an item from the set
    updated_set = remove_single_item(sample_set, 3)
    
    # Print the updated set
    print("Set after removing an item:", updated_set)

if __name__ == "__main__":
    main()
