'''

@Author: Jayesh Patil
@Date: 2024-08-13
@Last Modified by: Jayesh Patil
@Title : Print Documentation of Python Built-in Function


'''
def print_builtin_function_docs(function_name):


    """


    Description:
        Prints the documentation (syntax, description, etc.) of the specified Python built-in function.

    Parameters:
        function_name (str): The name of the Python built-in function.

    Return:
        None
    
    
    """
    
    try:
        print(eval(function_name).__doc__)
    except NameError:
        print(f"'{function_name}' is not a valid Python built-in function.")



def main():
    function_name = input("Enter the name of the Python built-in function: ")
    print_builtin_function_docs(function_name)

if __name__ == '__main__' :
    main()