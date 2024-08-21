'''

@Author: jayesh Patil
@Date: 2024-08-19
@Last Modified by: Jayesh Patil
@Title : program to create a symmetric difference.

'''
def symmetric_difference_of_sets(set1, set2):
    """
    Description :
        Creates a symmetric difference of two sets.

    Parameters:
        set1 (set): The first set.
        set2 (set): The second set.

    Returns:
        set: A set containing elements that are in either set1 or set2 but not in both.
    """
    return set1.symmetric_difference(set2)

def main():
    set_a = {1, 2, 3, 4, 5}
    set_b = {4, 5, 6, 7, 8}
    
    sym_diff_set = symmetric_difference_of_sets(set_a, set_b)
    
    print("Symmetric difference of set_a and set_b:", sym_diff_set)

if __name__ == "__main__":
    main()
