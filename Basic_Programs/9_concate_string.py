def concatenate_list(elements):
    
    """
    
    Concatenates all elements in a list into a single string.

    Parameters:
        elements (list): The list of elements to concatenate.

    Returns:
        str: A single string that is the concatenation of all elements in the list.
    
    
    """
    
    concatenated_string = ''
    
    for element in elements:
        concatenated_string += str(element)
    
    return concatenated_string


if __name__ == "__main__":
    elements = ['Hello', ' ', 'world', '!', ' ', 'Python', ' ', 'is', ' ', 'awesome']
    # elements = [123, 456, 6567, 34, 33]
    
    result = concatenate_list(elements)
    print("Concatenated String:", result)