'''


@Author: Jayesh Patil
@Date: 2024-08-13
@Last Modified by: Jayesh Patil
@Title : Print Calendar of Given Month and Year


'''

import calendar

def print_month_calendar(year, month):


    """
    
    
    Description:
        Prints the calendar for a specific month and year.

    Parameters:
        year (int): The year of the calendar.
        month (int): The month of the calendar.

    Return:
        None
    
    
    """

    print(calendar.month(year, month))

year = int(input("Enter the year (e.g., 2024): "))
month = int(input("Enter the month (1-12): "))
print_month_calendar(year, month)