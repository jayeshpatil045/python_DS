'''

@Author: Jayesh Patil
@Date: 2024-08-20
@Last Modified by: Jayesh Patil
@Title: Write a Python program to print a specified list after removing the 0th, 4th and
        5th elements.
        Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
        Expected Output : ['Green', 'White', 'Black']
'''
def remove_elements(sample_list, indices):
    """
    Description:
        Removes elements from the list at the specified indices.

    Parameters:
        sample_list (list): The original list from which elements will be removed.
        indices (list): A list of indices to be removed from the sample list.

    Returns:
         A new list with the specified elements removed.
    """
    return [item for i, item in enumerate(sample_list) if i not in indices]

def main():
    sample_list = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']

    indices_to_remove = [0, 4, 5]

    updated_list = remove_elements(sample_list, indices_to_remove)

    print("Updated List:", updated_list)

if __name__ == "__main__":
    main()
