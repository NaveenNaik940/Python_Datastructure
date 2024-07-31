'''

@Author:Naveen Madev Naik
@Date: 2024-07-26 10:13:00
@Last Modified by: Naveen Madev Naik
@Last Modified time: 2024-07-26 10:13:00
@Title :program to check whether a specified value is contained in a group of values

'''


def contains_value(value_list,check_value):


    """
    Description:
        Fuction will return true or false if value present in value list

    Parameter:
        value_list:contains list of value
        check_value:will check whether value_list contains this value
    Return:
        Boolean    
    """

    
    if check_value in value_list:
        return True
    else:
        return False

def main():
    try:
        no_of_values=int(input("enter the number of value you need to add: "))
        print(f"now add: ")
        value_list=[]
        for _ in range(no_of_values):
            value_list.append(int(input("")))
        print("here is your list")
        print(value_list)   
        check_value=int(input("Enter the number you want to check in list: ")) 
        if contains_value(value_list,check_value):
            print(f"{check_value} is present in list {value_list}")
        else:
             print(f"{check_value} is not present in list {value_list}")   
    except ValueError as e:
        print(f"you are getting {e}, integer values only")  

if __name__=="__main__":
    main()
