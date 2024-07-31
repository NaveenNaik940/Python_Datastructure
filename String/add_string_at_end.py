'''

@Author:Naveen Madev Naik
@Date: 2024-07-26 16:37:00
@Last Modified by: Naveen Madev Naik
@Last Modified time: 2024-07-26 16:37:00
@Title :program to add 'ing' at the end of a given string (length should be at
        least 3). If the given string already ends with 'ing' then add 'ly' instead. If the string length of the
        given string is less than 3, leave it unchanged.

'''


def add_string_at_end(word):
    
    
    """
    Description:
        Function will add the ing at the end of a given string (length should be at
        least 3) or If the given string already ends with 'ing' then add 'ly' instead. 
    Parameter:
        word:string of input from user
    return:
        string       
    """

    
    if len(word)<3:
        return word
    elif 'ing' in word[len(word)-3:len(word)]:
        word+="ly"
    else:
        word+="ing"
    return word        


def main():
    try:
        word=input("Enter the word to check frequency of character in word: ")
        print(f"after modifying'{word}': {add_string_at_end(word)}")

    except Exception as e:
        print(e)    

if __name__=="__main__":
    main()