'''

@Author:Naveen Madev Naik
@Date: 2024-07-26 15:51:00
@Last Modified by: Naveen Madev Naik
@Last Modified time: 2024-07-26 15:51:00
@Title :program to calculate the length of a string.

'''


def str_len(word):
    
    
    """
    Description:
        Function will return length of given word(string)
    Parameter:
        word:string of input from user
    return:
        int:length of word        
    """

    word_length=0
    for char in word:
        word_length+=1
    return word_length

def main():
    try:
        word=input("Enter the word to check its length: ")
        print(f"length of '{word}' is :{str_len(word)}")

    except Exception as e:
        print(e)    

if __name__=="__main__":
    main()