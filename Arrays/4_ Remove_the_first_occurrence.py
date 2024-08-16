def remove_first_occurrence(arr, element):
    """
    Removes the first occurrence of a specified element from an array.

    Parameters:
        arr (list): The list of integers from which the element will be removed.
        element (int): The element to remove from the list.

    Returns:
        list: The list with the first occurrence of the specified element removed.
    """
    
    if element in arr:
        
        arr.remove(element)
    return arr

def main():
    """
    Prompts the user for input, removes the first occurrence of a specified element from the array,
    and prints the modified array.
    """
    # Take array input from the user
    user_input = input("Enter the elements of the array separated by spaces: ")
    
    # Convert the input string into a list of integers
    arr = list(map(int, user_input.split()))
    
   
    element_to_remove = int(input("Enter the element to remove: "))
    
  
    print("Array after removing the first occurrence of the element:", remove_first_occurrence(arr, element_to_remove))

if __name__ == "__main__":
    main()
