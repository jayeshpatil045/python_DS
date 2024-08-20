'''
@Author: jayesh Patil
@Date: 2024-08-19
@Last Modified by: Jayesh Patil
@Title : Write a Python program to count the values associated with key in a
dictionary.

'''
def count_success(data):
    """
    Description :
    Counts the number of dictionaries where the 'success' key is True.

    Parameters:
        data (list): A list of dictionaries.

    Returns:
        int: The count of dictionaries with 'success' as True.
    """
    count = 0
    for item in data:
        if item.get('success') == True:
            count += 1
    return count

def main():
    # Sample data
    data = [
        {'id': 1, 'success': True, 'name': 'Lary'},
        {'id': 2, 'success': False, 'name': 'Rabi'},
        {'id': 3, 'success': True, 'name': 'Alex'}
    ]
    
    # Count the number of dictionaries with 'success' as True
    success_count = count_success(data)
    
    # Print the result
    print("Count of dictionaries with 'success' as True:", success_count)

if __name__ == "__main__":
    main()
