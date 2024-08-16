'''


@Author: Jayesh Patil
@Date: 2024-08-14
@Last Modified by: Jayesh Patil
@Title : Reverse First and Last Name


'''

def reverse_name(first_name, last_name):

    """
    
    
    Description:
        Reverses the order of the user's first and last name.

    Parameters:
        first_name (str): The user's first name.
        last_name (str): The user's last name.

    Return:
        str: The reversed name in the format "LastName FirstName".
    
    
    """
    
    return (f"{last_name} {first_name}")


def main():
    first_name = str(input("Enter your first name: "))
    last_name = str(input("Enter your last name: "))

    reversed_name = reverse_name(first_name, last_name)
    print(f"Reversed name: {reversed_name}")


if __name__ == '__main__' :
    main()