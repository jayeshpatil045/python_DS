'''

@Author: jayesh Patil
@Date: 2024-08-16
@Last Modified by: Jayesh Patil
@Title :  Write a Python script to add a key to a dictionary. 


'''
def dictionary(d, key , value ):
    """
    Description :
    Adds a new key-value pair to a dictionary.

    Parameters:
        d (dict): The dictionary to which the key-value pair will be added.
        key: The key to add.
        value: The value associated with the key.

    Returns:
        dict: The updated dictionary with the new key-value pair added.
    """
    # d[key] = value this another approch
    d.update({key: value})
    return d

def main():
    user_dictionary = {2:3,4:5}

    print(f"Dictionary {user_dictionary}")

    new_key = 7

    new_value = 8 

    updated_dictionary = dictionary(user_dictionary,new_key,new_value)

    print(f"Updated Dictionary{updated_dictionary}")

if __name__ == '__main__':
    main()    
