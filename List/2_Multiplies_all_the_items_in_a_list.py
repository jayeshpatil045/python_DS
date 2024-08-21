'''

@Author: Jayesh Patil
@Date: 2024-08-20
@Last Modified by: Jayesh Patil
@Title: Write a Python program to multiplies all the items in a list.


'''
def multiply_list(list1):
    """
    Description:

         Multiplies all the items in a list and returns the product.

    Parameters:
         items (list): A list of numbers to multiply.

    Returns:
          The product of all the numbers in the list.
    """
    product = 1
    for i in list1:
        product *= i
    return product
def main():
    list1 = [23,45,67,89,34]
    total_product = multiply_list(list1)
    print(f"Total Product of the list is {total_product}")
if __name__ == "__main__":
    main()


  