'''

@Author: jayesh Patil
@Date: 2024-08-16
@Last Modified by: Jayesh Patil
@Title :  Write a Python script to sort (ascending and descending) a dictionary by value


'''
def sort_dict_by_value(d, ascending=True):
    """
    Description :
    Sorts a dictionary by its values.

    Parameters:
        d (dict): The dictionary to sort.
        ascending (bool): If True, sorts in ascending order; if False, sorts in descending order.

    Returns:
        dict: A new dictionary sorted by values.
    """
    
    items = list(d.items())
    
    items.sort(key=lambda item: item[1], reverse=not ascending)
    
    sorted_dict = dict(items)
    
    return sorted_dict

def main():
    """
    Prompts the user for a dictionary input, sorts it by values in both ascending and descending order,
    and prints the sorted dictionaries.
    """
    # Take dictionary input from the user
    user_input = input("Enter a dictionary in the format {key1:value1, key2:value2, ...}: ")
    
   
    try:
        user_dict = eval(user_input)
        
        if not isinstance(user_dict, dict):
            raise ValueError("Input is not a valid dictionary.")
        
    except (SyntaxError, ValueError) as e:
        print(f"Invalid input: {e}")
        return

    print("\nOriginal dictionary:")
    print(user_dict)
    
    # Sort the dictionary in ascending order
    ascending_sorted_dict = sort_dict_by_value(user_dict, ascending=True)
    print("\nSorted dictionary in ascending order:")
    print(ascending_sorted_dict)
    
    # Sort the dictionary in descending order
    descending_sorted_dict = sort_dict_by_value(user_dict, ascending=False)
    print("\nSorted dictionary in descending order:")
    print(descending_sorted_dict)

# Call the main function to execute the script
if __name__ == "__main__":
    main()
