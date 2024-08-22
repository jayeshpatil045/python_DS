'''
@Author: jayesh Patil
@Date: 2024-08-19
@Last Modified by: Jayesh Patil
@Title : Write a Python program to convert a list into a nested dictionary of keys.

'''
def list_to_nested_dict(input_list):
    """
    Description :
    Converts a list into a nested dictionary of keys.

    Parameters:
        input_list (list): The list to be converted.

    Returns:
        dict: A nested dictionary where each element of the list is a key.
    """
    if not input_list:
        return {}
    
    nested_dict = {}
    current_level = nested_dict
    
    for key in input_list[:-1]:  
        current_level[key] = {}
        current_level = current_level[key]
    
    current_level[input_list[-1]] = {}
    
    return nested_dict

def main():
    # Sample list
    sample_list = ['a', 'b', 'c', 'd']
    
    result = list_to_nested_dict(sample_list)
    
    print(result)

if __name__ == "__main__":
    main()
