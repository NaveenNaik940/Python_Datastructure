'''

@Author:Naveen Madev Naik
@Date: 2024-07-26 16:56:00
@Last Modified by: Naveen Madev Naik
@Last Modified time: 2024-07-26 16:56:00
@Title :script that takes input from the user and displays that input back in
        upper and lower cases.

'''


def to_upper_lower_case(word):
    
    
    """
    Description:
        Function will take input from the user and displays that input back in
        upper and lower cases. 
    Parameter:
        word:input from user to convert it into upper and lower case
    Return:
        string       
    """


    return word.upper(),word.lower()

def main():
    try:
        word=input("enter the word toconvert it into upper and lower: ")
        upper_word,lower_word=to_upper_lower_case(word)
        print(f"The upper word: {upper_word}",f"The lower word: {lower_word}",sep="\n")

    except Exception as e:
        print(e)    

if __name__=="__main__":
    main()