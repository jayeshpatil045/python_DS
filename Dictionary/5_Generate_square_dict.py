'''
@Author: jayesh Patil
@Date: 2024-08-16
@Last Modified by: Jayesh Patil
@Title : Write a Python script to generate and print a dictionary that contains a 
         number (between 1 and n) in the form (x, x*x).  

'''
def generate_square_dict(n):
    """
    Description :
    Generates a dictionary with numbers from 1 to n as keys and their squares as values.

    Parameters:
        n (int): The upper limit of the range for dictionary keys.

    Returns:
        dict: A dictionary where each key is a number from 1 to n and the value is the square of the key.
    """
    return {x: x * x for x in range(1, n + 1)}

def main():
    """
    Demonstrates generating and printing a dictionary with numbers and their squares.
    """

    n = 5
    
    square_dict = generate_square_dict(n)
    
    print(f"Sample Dictionary (n = {n}):")
    print(square_dict)

if __name__ == "__main__":
    main()
