'''

@Author: Jayesh Patil
@Date: 2024-08-14
@Last Modified by: Jayesh Patil
@Title : Create and Display an Array of Integers in Python


'''

from array import array
def printarrays():
    int_array = [10,20,30,40,50]
    print("arrays :",int_array)
    for index in range(len(int_array)):
        print(f"Element at index{index}:{int_array[index]}")
printarrays()        