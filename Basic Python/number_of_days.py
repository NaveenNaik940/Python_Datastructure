'''

@Author:Naveen Madev Naik
@Date: 2024-07-25 15:13:00
@Last Modified by: Naveen Madev Naik
@Last Modified time: 2024-07-25 15:13:00
@Title :program to calculate number of days between two dates.

'''


def number_of_days(year_list,month_list,day_list):


    """
    
    Description:
        Calulates the number of days between Two given Dates 
    Parameter:
        year_list:list consist of year 1 and year 2 
        month_list: list consist of month 1 and month 2
        day_list: list consist of day 1 and day 2
    Return:
        None
    """
    
    
    no_of_days =abs((day_list[1]-day_list[0]) + (month_list[1]-month_list[0])*30 + (year_list[1] - year_list[0]) * 365)
    print(f"number of days between two provided dates{no_of_days}")


    
def main():
    try:
        print("Enter the First Date: ")
        year1 = int(input("Enter the 1st Year"))
        if year1<0:
            raise ValueError("year must be positive integer")
        month1 = int(input("Enter the 1st month "))
        if month1<1 and month1>12:
            raise ValueError("month must be between 1 and 12")   
        day1 = int(input("Enter the 1st date date"))
        if day1<1 and day1>31:
            raise ValueError("day should in range(1-31)") 
  
        print("\nEnter the Second Date: ")
        year2 = int(input("Enter the 2nt Year"))
        if year2<0:
            raise ValueError("year must be positive integer")
        month2 = int(input("Enter the 2nt month "))
        if month2<1 and month2>12:
            raise ValueError("month must be between 1 and 12")   
        day2 = int(input("Enter the 2nt date date"))
        if day2<1 and day2>31:
            raise ValueError("day should in range(1-31)") 
        
        
        year_list=[year1,year2] 
        month_list=[month1,month2]
        day_list=[day1,day2] 
        number_of_days(year_list,month_list,day_list)

    except ValueError as e:
        print(f"{e}")
        
if __name__=="__main__":
     main()

        
        