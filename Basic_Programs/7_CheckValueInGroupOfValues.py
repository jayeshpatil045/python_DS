'''

@Author: Jayesh Patil
@Date: 2024-08-16
@Last Modified by: Jayesh Patil
@Title : Check if Value is in a Group of Values


'''

def is_value_in_group(value, group):
    
    """
    
    Description:
        Checks whether a specified value is contained in a group of values.

    Parameters:
        value (int): The value to check.
        group (list): The group of values to check against.

    Return:
        bool: True if the value is in the group, False otherwise.
    
    
    """

    return value in group


try:
    value = int(input("Enter the value to check: "))
    group = input("Enter the group of values separated by spaces: ").split()
    
    group = [int(values) for values in group]
    

    result = is_value_in_group(value, group)
    print(f"{value} -> {group} : {result}")
except ValueError:
    print("Please enter valid integers for the value and group of values.")