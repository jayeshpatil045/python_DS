'''

@Author: Jayesh Patil
@Date: 2024-08-13
@Last Modified by: Jayesh Patil
@Title : Calculate Number of Days Between Two Dates


'''

from datetime import date

def calculate_days_between_dates(date1, date2):
    
    
    """
    
    
    Description:
        Calculates the number of days between two dates.

    Parameters:
        date1 (tuple): The first date in the format (year, month, day).
        date2 (tuple): The second date in the format (year, month, day).

    Return:
        int: The number of days between the two dates.
    
    
    """


    d1 = date(date1[0], date1[1], date1[2])
    d2 = date(date2[0], date2[1], date2[2])
    difference = d2 - d1

    return difference.days



date1 = (2014, 7, 1)
date2 = (2014, 7, 12)
days_between = calculate_days_between_dates(date1, date2)
print(f"{days_between} days")