'''

@Author:Naveen Madev Naik
@Date: 2024-07-29 16:00:00
@Last Modified by: Naveen Madev Naik
@Last Modified time: 2024-07-29 16:00:00
@Title :program to split a list based on first character of word.

'''


def split_by_first_character(words):


    """
    Description:
        Split a list of words into sublists based on the first character of each word.

    Parameters:
        words (list): A list of strings.

    Returns:
        dict: A dictionary where the keys are characters and the values are lists of words starting with that character.
    """
    
    
    grouped_words = {}

    for word in words:
        if word:  
            first_char = word[0]  
            if first_char not in grouped_words:
                grouped_words[first_char] = []
            grouped_words[first_char].append(word)

    return grouped_words

def main():
    try:
        no_of_element=int(input("eneter the number of element in the list: "))
        words = []
        print("add words one by one")
        for index in range(no_of_element):
            words.append(input(": "))
        
        result = split_by_first_character(words)
        
        for char, words_list in result.items():
            print(f"{char}: {words_list}")

    except ValueError as e:
        print(e)        

if __name__ == "__main__":
    main()
