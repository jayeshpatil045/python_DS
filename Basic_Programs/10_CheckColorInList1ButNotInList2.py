'''


@Author: Jayesh Patil
@Date: 2024-08-16
@Last Modified by: jayesh Patil
@Title : Colors in color_list_1 but not in color_list_2


'''


def get_unique_colors(color_list_1, color_list_2):
    
    """
    
    
    Description:
        Returns a set of colors that are in color_list_1 but not in color_list_2.

    Parameters:
        color_list_1 (set): The first set of colors.
        color_list_2 (set): The second set of colors.

    Return:
        set: A set of colors from color_list_1 that are not in color_list_2.
    
    
    """
    
    
    return color_list_1.difference(color_list_2)

if __name__ == "__main__":
    color_list_1 = set(["White", "Black", "Red"])
    color_list_2 = set(["Red", "Green"])

    unique_colors = get_unique_colors(color_list_1, color_list_2)
    print(unique_colors)    