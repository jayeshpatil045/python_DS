'''
@Author: jayesh Patil
@Date: 2024-08-16
@Last Modified by: Jayesh Patil
@Title :  Write a Python program to remove a key from a dictionary.

'''
def remove_key_from_dict(d, key):
    """
    Description :
    Removes a specified key from the dictionary using the del statement.

    Parameters:
        d (dict): The dictionary from which the key will be removed.
        key: The key to remove.

    Returns:
        dict: The dictionary after the key has been removed.
    """
    if key in d:
         d[key]
    return d

def main():
    """
    Demonstrates removing a key from a sample dictionary and prints the results.
    """
    sample_dict = {
        'name': 'Tom',
        'age': 25,
        'city': 'pune',
        'occupation': 'Engineer'
    }
    
    print(f"Original dictionary:{sample_dict}")
    
    
    key_to_remove = 'city'
    
    updated_dict = remove_key_from_dict(sample_dict, key_to_remove)
    
    print(f"\nDictionary after removing the key '{key_to_remove}':")
    print(updated_dict)

if __name__ == "__main__":
    main()
