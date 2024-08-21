'''

@Author: Jayesh Patil
@Date: 2024-08-20
@Last Modified by: Jayesh Patil
@Title: Write a Python program to generate all permutations of a list in Python.
'''
def permute(current_list):
    """
     Description:
        Recursively generates all permutations of the current list.

    Parameters:
        current_list (list): The list of elements to generate permutations from.

    Returns:
        A list of lists, each containing a permutation of the current list.
    """
    if len(current_list) == 0:
        return []
    
    if len(current_list) == 1:
        return [current_list]

    result = []

    for i in range(len(current_list)):
        current_element = current_list[i]

        remaining_list = current_list[:i] + current_list[i+1:]

        for p in permute(remaining_list):
            result.append([current_element] + p)

    return result

def main():
    sample_list = [1, 2, 3]

    permutations = permute(sample_list)

    print("All permutations of the list:")
    for perm in permutations:
        print(perm)

if __name__ == "__main__":
    main()
