'''

@Author:Naveen Madev Naik
@Date: 2024-07-25 15:13:00
@Last Modified by: Naveen Madev Naik
@Last Modified time: 2024-07-25 15:13:00
@Title :program to print the calendar of a given month and year

'''


import calendar

def print_calendar(month,year):


    """
    Description:
         Function will print the given year and month calender
    Parameter:
        month:which will be used to get the calendar
        year: which will be used to get the calendar
    return:
        none        
    """

    
    # Create a TextCalendar instance
    text_cal = calendar.TextCalendar(firstweekday=6)

    # Print the calendar for year and month
    
    print(text_cal.formatmonth(year,month))
    
def main():
    # Input from the user
    try:
        month=int(input("enter the month to show calender: "))
        year=int(input("Enter the year to show calender: "))
        if year<0:
            raise ValueError("year should not be negative number")
        if month>12 and month<1:
            raise ValueError("Month should be between 1 and 12")
        
        print_calendar(year,month)
    except ValueError:
        print(f"enter valid integer number")

if __name__=="__main__":
    main()    
        
        