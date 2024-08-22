'''

@Author: jayesh Patil
@Date: 2024-08-19
@Last Modified by: Jayesh Patil
@Title : Python program to add member(s) in a set..

'''
def add_single_member(my_set, element):
    """
    Description :
         Adds a single element to the set.

    Parameters:
        my_set (set): The set to which the element will be added.
        element: The element to add to the set.

    Returns:
        set: The set after the element has been added.
    """
    my_set.add(element)
    return my_set

def main():
    
    sample_set = {1, 2, 3}
    

    updated_set = add_single_member(sample_set, 4)
    
    # Print the updated set
    print("Set after adding a single member:", updated_set)

if __name__ == "__main__":
    main()
