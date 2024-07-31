'''

@Author:Naveen Madev Naik
@Date: 2024-07-27 11:50:00
@Last Modified by: Naveen Madev Naik
@Last Modified time: 2024-07-27 11:50:00
@Title :program to lowercase first n characters in a string.

'''


def lowercase_n_char(main_string,n):
    

    """
    Description:
        Function will lowercasethe first n char in string
    Parameter:
        main_string:user given main string 
        n:lower case the first n char in string    
    Return:
        String   
    """


    string_length=len(main_string)
    lowercase_string=""+main_string[:n].lower()+main_string[n:string_length]
    return lowercase_string

def main():
    try:
        main_string = input("Enter the string consist of all upeercase letter: ")
        n_char=int(input("enter the number of char you wnat to lowercase: "))
        if n_char>len(main_string):
            raise ValueError("given length of char should be less than main string length")
        print(f"after lowering the first {n_char} char in  {main_string} is : {lowercase_n_char(main_string,n_char)}")

    except ValueError as e:
        print(f"{e}")    

if __name__ == "__main__":
    main()
