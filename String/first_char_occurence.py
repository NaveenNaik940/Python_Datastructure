'''

@Author:Naveen Madev Naik
@Date: 2024-07-26 16:18:00
@Last Modified by: Naveen Madev Naik
@Last Modified time: 2024-07-26 16:18:00
@Title :program to get a string from a given string where all occurrences of its
        first char have been changed to '$', except the first char itself.

'''


def change_repetitive_first_char(word,character):
    
    
    """
    Description:
        from a given string where all occurrences of its
        first char have been changed to '$', except the first char itself.
    Parameter:
        word:string of input from user
    return:
        string       
    """

    
    first_char=word[0]
    changed_word=word[0]
    for char in word[1:]:
        if char in first_char:
            changed_word+=character
        else:
            changed_word+=char

    return changed_word        



def main():
    try:
        word=input("Enter the word  ")
        character="$"
        print(f"after all occurrences of its first char have been changed to {character}: {change_repetitive_first_char(word,character)}")

    except Exception as e:
        print(e)    

if __name__=="__main__":
    main()