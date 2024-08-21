'''
@Author: Jayesh Patil
@Date: 2024-08-20
@Last Modified by: Jayesh Patil
@Title: Write a Python program to get a list, sorted in increasing order by the last
        element in each tuple from a given list of non-empty tuples.
        Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
        Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]
'''
def list_sorted(tuples):
    """
    Description:
        Sorts a list of non-empty tuples in increasing order by the last element in each tuple.

    Parameters:
        tuples (list): A list of non-empty tuples to sort.

    Returns:
        list: A list of tuples sorted by the last element in each tuple.
    """

    return sorted(tuples, key= lambda x:x[-1] )

def main():
     sample_list = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
     result = list_sorted(sample_list)
     print(f"The given list {sample_list}and sorted list{result}")

if __name__ == "__main__":
    main()
