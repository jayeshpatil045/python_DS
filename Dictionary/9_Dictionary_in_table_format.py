'''
@Author: jayesh Patil
@Date: 2024-08-19
@Last Modified by: Jayesh Patil
@Title : Write a Python program to print a dictionary in table format.

'''
def print_dict_table(input_dict):
    """
    Description :
    Prints a dictionary in table format.

    Parameters:
        input_dict (dict): The dictionary to be printed.
    """
   
    key_width = max(len(str(key)) for key in input_dict.keys()) + 2
    value_width = max(len(str(value)) for value in input_dict.values()) + 2

    # Print the header
    print(f"{'Key'.ljust(key_width)}| {'Value'.ljust(value_width)}")
    print("-" * (key_width + value_width + 3))

    # Print each key-value pair
    for key, value in input_dict.items():
        print(f"{str(key).ljust(key_width)}| {str(value).ljust(value_width)}")

def main():
    
    sample_dict = {
        'Name': 'John',
        'Age': 25,
        'Occupation': 'Software Engineer',
        'Country': 'pune'
    }
    
    print_dict_table(sample_dict)

if __name__ == "__main__":
    main()
