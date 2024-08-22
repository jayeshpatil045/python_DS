'''
@Author: jayesh Patil
@Date: 2024-08-19
@Last Modified by: Jayesh Patil
@Title :  Write a Python program to find unique values

'''
def unique_values(data):
    """
    Description :
    Finds and returns unique values from a list of dictionaries.

    Parameters:
        data (list): A list of dictionaries to extract unique values from.

    Returns:
        set: A set of unique values.
    """
    unique_set = set()
    for dictionary in data:
        for value in dictionary.values():
            unique_set.add(value)
    return unique_set

def main():
    """
    Demonstrates finding unique values from sample data and prints the results.
    """
    # Sample data
    data = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"},
            {"VII": "S005"}, {"V": "S009"}, {"VIII": "S007"}]
    
    # Get unique values
    unique_vals = unique_values(data)
    
    print("Unique Values:", unique_vals)

if __name__ == "__main__":
    main()
