'''
@Author: jayesh Patil
@Date: 2024-08-20
@Last Modified by: Jayesh Patil
@Title : Python program to slice a tuple.

'''
def slice_tuple(t, start, end, step=1):
    """
    Description :
        Slices a tuple based on the provided indices and step.

    Parameters:
        t (tuple): The tuple to be sliced.
        start (int): The starting index of the slice.
        end (int): The ending index of the slice (non-inclusive).
        step (int): The step value for slicing. Defaults to 1.

    Returns:
        tuple: A new tuple that is a slice of the original tuple.
    """
    return t[start:end:step]

def main():
    my_tuple = (10, 20, 30, 40, 50, 60, 70, 80, 90)

    start_index = 2
    end_index = 7
    step_value = 2

    sliced_tuple = slice_tuple(my_tuple, start_index, end_index, step_value)

    print("Original tuple:", my_tuple)
    print("Sliced tuple:", sliced_tuple)

if __name__ == "__main__":
    main()
