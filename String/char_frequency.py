'''

@Author:Naveen Madev Naik
@Date: 2024-07-26 15:51:00
@Last Modified by: Naveen Madev Naik
@Last Modified time: 2024-07-26 15:51:00
@Title :program to count the number of characters (character frequency) in a
        string.

'''


def char_frequency(word):
    
    
    """
    Description:
        Function will return frequency of character in word
    Parameter:
        word:string of input from user
    return:
        dict       
    """

    
    frequency_dict={}
    for char in word:
        if char in frequency_dict:
            frequency_dict[char]+=1
        else:
            frequency_dict[char]=1 
    
    return frequency_dict


def main():
    try:
        word=input("Enter the word to check frequency of character in word: ")
        print(f"frquency of character in '{word}': {char_frequency(word)}")

    except Exception as e:
        print(e)    

if __name__=="__main__":
    main()