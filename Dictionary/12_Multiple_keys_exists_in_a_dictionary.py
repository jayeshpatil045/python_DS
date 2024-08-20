'''
@Author: jayesh Patil
@Date: 2024-08-19
@Last Modified by: Jayesh Patil
@Title : Write a Python program to check multiple keys exists in a dictionary.

'''
def check_keys_exist(dictionary, keys):
    """
    Description :
    Checks if multiple keys exist in a dictionary.

    Parameters:
        dictionary (dict): The dictionary to check.
        keys (list): A list of keys to check for.

    Returns:
        bool: True if all keys exist in the dictionary, False otherwise.
    """
    return all(key in dictionary for key in keys)

def main():
    # Sample dictionary
    sample_dict = {
        'name': 'John',
        'age': 30,
        'occupation': 'Engineer',
        'country': 'USA'
    }

    # Keys to check
    keys_to_check = ['name', 'age', 'country']
    
    # Check if all keys exist in the dictionary
    result = check_keys_exist(sample_dict, keys_to_check)
    
    # Print the result
    if result:
        print("All keys exist in the dictionary.")
    else:
        print("Not all keys exist in the dictionary.")

if __name__ == "__main__":
    main()
