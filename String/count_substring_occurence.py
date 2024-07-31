'''

@Author:Naveen Madev Naik
@Date: 2024-07-27 11:30:00
@Last Modified by: Naveen Madev Naik
@Last Modified time: 2024-07-27 11:30:00
@Title :program to count occurrences of a substring in a string.

'''


def count_substring_occurrences(main_string, substring):
    

    """
    Description:
        Function will return the count of number substring occured in  given main string
    Parameter:
        main_string:user given main string
        substring: user given substring to find its occurence in main string
    Return:
        int    
    """

    
    count = main_string.count(substring)
    return count

def main():
    main_string = input("Enter the main string: ")
    substring = input("Enter the substring to count: ")
    
    occurrences = count_substring_occurrences(main_string, substring)
    print(f"The substring '{substring}' occurs {occurrences} times in the main string.")

if __name__ == "__main__":
    main()
