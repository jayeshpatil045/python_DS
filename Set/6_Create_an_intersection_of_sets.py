'''

@Author: jayesh Patil
@Date: 2024-08-19
@Last Modified by: Jayesh Patil
@Title : Python program to create an intersection of sets.

'''
def intersection_of_sets(set1, set2):
    """
    Description : 
        Creates an intersection of two sets.

    Parameters:
        set1 (set): The first set.
        set2 (set): The second set.

    Returns:
        set: A set containing the intersection of set1 and set2.
    """
    return set1.intersection(set2)

def main():
    
    set_a = {1, 2, 3, 4, 5}
    set_b = {3, 4, 5, 6, 7}
    
    intersected_set = intersection_of_sets(set_a, set_b)
    
    print("Intersection of set_a and set_b:", intersected_set)

if __name__ == "__main__":
    main()
