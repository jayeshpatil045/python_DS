'''

@Author: jayesh Patil
@Date: 2024-08-16
@Last Modified by: Jayesh Patil
@Title : Write a Python program to iterate over dictionaries using for loops. 


'''
def iterate_dict(d):
    """
    Description :
    Iterates over a dictionary and demonstrates different ways to access keys and values.

    Parameters:
        d (dict): The dictionary to iterate over.
    """
    print("Iterating over keys:")
    for key in d:
        print(f"Key: {key}")

    print("\nIterating over values:")
    for value in d.values():
        print(f"Value: {value}")

    print("\nIterating over key-value pairs:")
    for key, value in d.items():
        print(f"Key: {key}, Value: {value}")

def main():
    """
    Demonstrates iteration over a sample dictionary and prints the results.
    """
    
    sample_dict = {
        'name': 'joy',
        'age': 24,
        'city': 'pune',
        'occupation': 'Engineer'
    }
    
    print("Sample dictionary:")
    print(sample_dict)
    

    iterate_dict(sample_dict)


if __name__ == "__main__":
    main()
