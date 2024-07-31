'''

@Author:Naveen Madev Naik
@Date: 2024-07-26 16:56:00
@Last Modified by: Naveen Madev Naik
@Last Modified time: 2024-07-26 16:56:00
@Title :program that accepts a comma separated sequence of words as input
        and prints the unique words in sorted form (alphanumerically).

'''


def sorted_unique_word(word):
    
    
    """
    Description:
        Function will accepts a comma separated sequence of words as input
        and prints the unique words in sorted form. 
    Parameter:
        word:input from user 
    Return:
        string       
    """


    word_set=set(word.split(","))
    word_set={word.strip() for word in word_set if word.strip()}
    word_list=sorted(word_set)
    sorted_word=", ".join(word_list)

    return sorted_word    


def main():
    try:
        word=input("enter the comma seperated word: ")
        
        print(f"Unique words after sorting : {sorted_unique_word(word)}")

    except Exception as e:
        print(e)    

if __name__=="__main__":
    main()