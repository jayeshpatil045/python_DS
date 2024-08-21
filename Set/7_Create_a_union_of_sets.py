'''

@Author: jayesh Patil
@Date: 2024-08-19
@Last Modified by: Jayesh Patil
@Title : Python program to create a union of sets.

'''
def union_of_sets(set1, set2):
    """
    Description :
        Creates a union of two sets.

    Parameters:
        set1 (set): The first set.
        set2 (set): The second set.

    Returns:
        set: A set containing the union of set1 and set2.
    """
    return set1.union(set2)

def main():
    set_a = {1, 2, 3, 4, 5}
    set_b = {4, 5, 6, 7, 8}
    
   
    union_set = union_of_sets(set_a, set_b)
    
    print("Union of set_a and set_b:", union_set)

if __name__ == "__main__":
    main()
