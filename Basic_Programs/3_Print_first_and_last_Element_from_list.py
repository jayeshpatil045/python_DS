'''


@Author: Jayesh Patil
@Date: 2024-08-14
@Last Modified by: Jayesh Patil
@Last Modified time: 2024-08-14
@Title : Display First and Last Color from List


'''


def display_color(color_list):
    
    """
    
    Description:
        Returns the first and last color from a given list of colors.

    Parameters:
        color_list (list): A list containing color names.

    Return:
        str: A string containing the first and last color separated by a comma.
    
    
    """
    
    return f"{color_list[0]}, {color_list[-1]}"

def main():
    color_list = ["Red","Green", "Yellow", "Voilet", "White" ,"Black"]
    result = display_color(color_list)
    print(f"Selected colors: {result}")


if __name__ == '__main__' :
    main()