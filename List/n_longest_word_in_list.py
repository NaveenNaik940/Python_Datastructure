'''

@Author:Naveen Madev Naik
@Date: 2024-07-29 12:44:00
@Last Modified by: Naveen Madev Naik
@Last Modified time: 2024-07-29 12:44:00
@Title :program to find the list of words that are longer than n from a
        given list of words.

'''


def filter_long_words(words_list, min_length):


    """
    Description:
        Filters words from the list that are longer than a given length.
    
    Parameters:
        words_list (list of str): The list of words to filter.
        min_length (int): The minimum length of words to include in the result.
    
    Returns:
        list of str: A list of words longer than the specified length.
    """


    long_words = [word for word in words_list if len(word) > min_length]
    
    return long_words

def main():
    
    try:
        no_of_element = int(input("Enter the number element in the list: "))
        example_list=[]
        print("enter the element i the list one by one")
        for element in range(no_of_element):
            example_list.append(input(": "))
        min_length = int(input("Enter the minimum length of words to filter: "))
    
        result = filter_long_words(example_list, min_length)
        
        print(f"Words longer than {min_length}: {result}")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
