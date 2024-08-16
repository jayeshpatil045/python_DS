'''


@Author: Jayesh Patil
@Date: 2024-08-13
@Last Modified by: Jayesh Patil
@Title : Check if File Exists


'''

import os

def check_file_exists(file_path):

    """
    
    
    Description:
        Checks whether a file exists at the given file path.

    Parameters:
        file_path (str): The path of the file to check.

    Return:
        bool: True if the file exists, False otherwise.
    
    
    """
    
    return os.path.isfile(file_path)


if __name__ == "__main__":
    file_path = input("Enter the file path to check: ")
    if check_file_exists(file_path):
        print(f"The file '{file_path}' exists.")
    else:
        print(f"The file '{file_path}' does not exist.")