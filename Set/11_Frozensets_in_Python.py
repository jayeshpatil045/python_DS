'''

@Author: jayesh Patil
@Date: 2024-08-19
@Last Modified by: Jayesh Patil
@Title : Write a Python program to clear a set.

'''

def demonstrate_frozenset():
    """
    Description :
        Demonstrates the use of frozensets in Python.
    """
    
    frozen_set_a = frozenset([1, 2, 3, 4, 5])
    frozen_set_b = frozenset([4, 5, 6, 7, 8])
    
    print("Frozen Set A:", frozen_set_a)
    print("Frozen Set B:", frozen_set_b)
    
    union_set = frozen_set_a.union(frozen_set_b)
    print("Union of Frozen Set A and B:", union_set)
    
    intersection_set = frozen_set_a.intersection(frozen_set_b)
    print("Intersection of Frozen Set A and B:", intersection_set)
    
    difference_set = frozen_set_a.difference(frozen_set_b)
    print("Difference of Frozen Set A and B (A - B):", difference_set)
    
    symmetric_difference_set = frozen_set_a.symmetric_difference(frozen_set_b)
    print("Symmetric Difference of Frozen Set A and B:", symmetric_difference_set)
    
    try:
        frozen_set_a.add(6)
    except AttributeError as e:
        print("Error: Cannot add elements to a frozenset -", e)
    
    try:
        frozen_set_a.remove(2)
    except AttributeError as e:
        print("Error: Cannot remove elements from a frozenset -", e)

def main():
    demonstrate_frozenset()

if __name__ == "__main__":
    main()
