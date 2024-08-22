'''

@Author: jayesh Patil
@Date: 2024-08-16
@Last Modified by: Jayesh Patil
@Title :   Write a Python script to concatenate following dictionaries to create a new one. 


'''
def concatenate_dictionaries(dict1,dict2,dict3):
    """
    Description :
    Concatenates multiple dictionaries into a new dictionary using the merge operator.

    Parameters:
        dic1 (dict): The first dictionary.
        dic2 (dict): The second dictionary.
        dic3 (dict): The third dictionary.

    Returns:
        dict: A new dictionary containing all key-value pairs from the input dictionaries.
    """
    return dict1 | dict2 | dict3 

def main():
    dict1 = {1:10, 2:20}
    dict2 = {3:30, 4:40}
    dict3 = {5:50, 6:60}

    merge_dict = concatenate_dictionaries(dict1,dict2,dict3)

    print(f"concatenate_dictionarie{merge_dict}")

if __name__ == '__main__':
    main()    

