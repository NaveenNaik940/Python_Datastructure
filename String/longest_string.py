'''

@Author:Naveen Madev Naik
@Date: 2024-07-26 16:45:00
@Last Modified by: Naveen Madev Naik
@Last Modified time: 2024-07-26 16:45:00
@Title :function that takes a list of words and returns the length of the longest one.

'''


def longest_string(word_list):
    
    
    """
    Description:
        Function will take the list of words and returns the length of the longest one. 
    Parameter:
        word_list:string of list, input from user
    return:
        string       
    """

    length=0
    for word in word_list:
        if length<len(word):
            length=len(word)
            longest_word=word

    return longest_word        


def main():
    try:
        number_of_word=int(input("enter the number word you want to add in list: "))
        word_list=[]
        for _ in range(number_of_word):
            word_list.append(input("enter word: "))

        print(f"The longest word in {word_list}: {longest_string(word_list)}")

    except Exception as e:
        print(e)    

if __name__=="__main__":
    main()