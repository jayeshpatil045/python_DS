'''
@Author: jayesh Patil
@Date: 2024-08-19
@Last Modified by: Jayesh Patil
@Title :  Write a Python program to count number of items in a dictionary value
          that is a list.

'''
def count_items_in_lists(dictionary):
    """
    Description :
    Counts the total number of items in a dictionary where the values are lists.

    Parameters:
        dictionary (dict): The dictionary with lists as values.

    Returns:
        int: The total number of items in all the lists.
    """
    total_count = 0
    for key, value in dictionary.items():
        if isinstance(value, list):
            total_count += len(value)
    return total_count

def main():
    # Sample dictionary
    sample_dict = {
        'fruits': ['apple', 'banana', 'cherry'],
        'vegetables': ['carrot', 'spinach'],
        'grains': ['rice', 'wheat', 'oats', 'quinoa'],
        'dairy': 'milk',  # Not a list, so should not be counted
    }
    
    # Count the total number of items in list values
    total_items = count_items_in_lists(sample_dict)
    
    # Print the result
    print("Total number of items in list values:", total_items)

if __name__ == "__main__":
    main()
