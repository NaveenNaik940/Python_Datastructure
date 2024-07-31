'''

@Author:Naveen Madev Naik
@Date: 2024-07-27 11:50:00
@Last Modified by: Naveen Madev Naik
@Last Modified time: 2024-07-27 11:50:00
@Title :program to reverse a string.

'''


def reverse_string(main_string):
    

    """
    Description:
        Function will return reversed string
    Parameter:
        main_string:user given main string 
        
    Return:
        String   
    """


    reversed_string=""
    for char in range(len(main_string)-1,-1,-1):
        reversed_string+=main_string[char]
    return reversed_string

def main():
    try:
        main_string = input("Enter the main string: ")
        print(f"reversed string of {main_string} is : {reverse_string(main_string)}")

    except Exception as e:
        print(f"{e}")    

if __name__ == "__main__":
    main()
