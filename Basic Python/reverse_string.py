'''

@Author:Naveen Madev Naik
@Date: 2024-07-25 12:23:00
@Last Modified by: Naveen Madev Naik
@Last Modified time: 2024-07-25 12:23:00
@Title :Python program which accepts the user's first and last name and print them in
reverse order with a space between them

'''


def reverse_username(firstName,lastName):


    """
    Description:
           function will return the reversed username

    Parameter:
        firstName:takes user's first name 
        lastName: takes user's last name

    return:
        string: returns the reversed user name        
    """


    return lastName+" "+firstName

def main():
    # Input from the user
    try:
        firstName= input("Enter Your first name:")
        lastName=input("Enter your last name: ")
        print(f"Hi {reverse_username(firstName,lastName)}")
        
    except Exception as e:
        print("e")

if __name__=="__main__":
    main()