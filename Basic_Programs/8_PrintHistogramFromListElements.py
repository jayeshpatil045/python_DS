'''


@Author: Jayesh Patil
@Date: 2024-08-16
@Last Modified by: Jayesh Patil
@Title : Print a Histogram from list of elements


'''
def histogram(data):
    """

    Creates a text-based histogram from a given list of integers.

    Parameters:
        data (list of int): The list of integers to be plotted in the histogram.

    Returns:
        None
    
    
    """
    max_value = max(data)
    frequency = {}
    for number in data:
        if number in frequency:
            frequency[number] +=1
        else:
            frequency[number] = 1
    print("Value | Frequency")
    for value, count in sorted(frequency.items()):
        print(f"{value:5} | {'*' * count}")

        

if __name__ == "__main__":
    data = [10, 20, 20, 30, 40, 50, 50, 50, 60, 70, 80, 90, 100]

    histogram(data)

