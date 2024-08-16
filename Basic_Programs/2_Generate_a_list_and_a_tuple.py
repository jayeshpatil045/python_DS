'''

@Author: Jayesh Patil
@Date: 2024-08-13
@Last Modified by: Jayesh Patil
@Title : Generate List and Tuple from Comma-Separated Numbers


'''

def generate_list_and_tuple(numbers):
    
    """
    
    
    Description:
        Converts a comma-separated string of numbers into a list and a tuple.

    Parameters:
        numbers (str): A string of comma-separated numbers.

    Return:
        tuple: A list and a tuple containing the numbers as strings.
    
    
    """


    number_list = numbers.split(",")
    
    number_tuple = tuple(number_list)
    
    return number_list, number_tuple



def main():
    numbers = input("Enter a sequence of comma-separated numbers : ")

    list_result, tuple_result = generate_list_and_tuple(numbers)

    print(f"List: {list_result}")
    print(f"Tuple: {tuple_result}")


if __name__ == '__main__' :
    main()