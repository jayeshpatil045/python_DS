'''

@Author: jayesh Patil
@Date: 2024-08-16
@Last Modified by: Jayesh Patil
@Title : Reverse the Order of Items in an Array in Python


'''
def count_occurrences(arr, element):
    """
    Calculates the most frequently occurring number in an array.

    Parameters:
        arr (list): A list of integers where the occurrences of each element are to be counted.

    Returns:
        int: The most frequently occurring number in the array.
        int: The number of times the most frequently occurring number appears in the array.
    """
    return arr.count(element)

def main():
    
    user_input = input("Enter the elements of the array separated by spaces: ")
    
    
    arr = list(map(int, user_input.split()))
    
    
    element_to_count = int(input("Enter the element to count its occurrences: "))
    
    
    occurrences = count_occurrences(arr, element_to_count)
    
    
    print(f"The element {element_to_count} occurs {occurrences} times in the array.")


if __name__ == "__main__":
    main()
