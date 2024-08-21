'''

@Author: jayesh Patil
@Date: 2024-08-19
@Last Modified by: Jayesh Patil
@Title : Python program to create set difference.

'''
def difference_of_sets(set1, set2):
    """
    Description :
       Creates a difference of two sets.

    Parameters:
        set1 (set): The first set.
        set2 (set): The second set.

    Returns:
        set: A set containing elements that are in set1 but not in set2.
    """
    return set1.difference(set2)

def main():
    # Sample sets
    set_a = {1, 2, 3, 4, 5}
    set_b = {4, 5, 6, 7, 8}
    
    # Get the difference of the two sets (set_a - set_b)
    difference_set = difference_of_sets(set_a, set_b)
    
    # Print the resulting difference set
    print("Difference of set_a and set_b (set_a - set_b):", difference_set)

if __name__ == "__main__":
    main()
