'''

@Author:Naveen Madev Naik
@Date: 2024-07-27 11:00:00
@Last Modified by: Naveen Madev Naik
@Last Modified time: 2024-07-27 11:00:00
@Title :program to get the last part of a string before a specified character

'''


def get_last_part_before_char(input_string, char):


    """
    Description:
        Function will return last part of the string before specified character
    Parameter:
        input_string: it is user input
        char: User specified character to get the last part of input string
    Return:
        String    
    """

    
    # Split the string from the right using the specified character
    parts = input_string.rsplit(char, 1)
    
    if len(parts) > 1:
        return parts[0]
    else:
        return input_string

def main():
    try:
        input_string=input("Enter the input string: ")
        specified_char=input("Enter thenspecific character: ")
        result = get_last_part_before_char(input_string, specified_char)
        print(f"The last part of the string before '{specified_char}' is: '{result}'")
    
    except Exception as e:
        print(f"{e}")

if __name__=="__main__":
    main()