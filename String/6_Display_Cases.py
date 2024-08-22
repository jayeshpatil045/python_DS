'''

@Author: Jayesh Patil
@Date: 2024-08-21
@Last Modified by: Jayesh Patil
@Title: Write a Python script that takes input from the user and displays that input back in upper and lower cases.
'''
def display_cases(user_input):
    """
    Description:
        Displays the input string in both upper and lower cases.

    Parameters:
        user_input (str): The string input by the user.

    Returns:
        A tuple containing the string in uppercase and lowercase.
    """
    upper_case = user_input.upper()
    lower_case = user_input.lower()
    return upper_case, lower_case

def main():
    user_input = input("Please enter a string: ")
    
    upper_case, lower_case = display_cases(user_input)
    
    print("Uppercase:", upper_case)
    print("Lowercase:", lower_case)

if __name__ == "__main__":
    main()
