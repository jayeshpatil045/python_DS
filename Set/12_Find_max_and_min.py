'''

@Author: jayesh Patil
@Date: 2024-08-19
@Last Modified by: Jayesh Patil
@Title : Finds the maximum and minimum values in a set.

'''
def find_max_min(my_set):
    """
    Description :
        Finds the maximum and minimum values in a set.

    Parameters:
        my_set (set): The set of numbers to find the max and min from.

    Returns:
        tuple: A tuple containing the maximum and minimum values in the set.
    """
    max_value = max(my_set)
    min_value = min(my_set)
    return max_value, min_value

def main():
    # Sample set
    sample_set = {23, 1, 45, 78, 3, 99, 4, 56}
    
    max_value, min_value = find_max_min(sample_set)
    
    print("Maximum value in the set:", max_value)
    print("Minimum value in the set:", min_value)

if __name__ == "__main__":
    main()
