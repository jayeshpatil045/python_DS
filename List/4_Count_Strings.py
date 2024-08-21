'''

@Author: Jayesh Patil
@Date: 2024-08-20
@Last Modified by: Jayesh Patil
@Title: Write a Python program to count the number of strings where the string length
        is 2 or more and the first and last character are same from a given list of strings.
        Sample List : ['abc', 'xyz', 'aba', '1221']
        Expected Result : 2


'''
def Count_Strings(string1):
    """
    Description:
            Counts the number of strings in the list where the string length is 2 or more 
            and the first and last character are the same.

    Parameters:
            strings (list): A list of strings to evaluate.

    Returns:
            The count of strings that meet the conditions.
    """
    count = 0
    for string in string1:
        if len(string) >= 2 and string[0] == string[-1]:
            count +=1
    return count 

def main():
    string1 =  ['abc', 'xyz', 'aba', '1221']
    result = Count_Strings(string1)
    print(f"The number of strings that meet the criteria is:{result}")

if __name__ == "__main__":
    main()