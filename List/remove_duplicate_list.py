'''

@Author:Naveen Madev Naik
@Date: 2024-07-29 16:00:00
@Last Modified by: Naveen Madev Naik
@Last Modified time: 2024-07-29 16:00:00
@Title :program to split a list based on first character of word.

'''


def remove_duplicates(list_of_lists):


    """
    Description:
        Remove duplicates from a list of lists.

    Parameters:
        list_of_lists (list of lists): The original list containing possible duplicates.

    Returns:
        list of lists: A new list with duplicates removed.
    """


    
    set_of_tuples = {tuple(inner_list) for inner_list in list_of_lists}

    unique_list_of_lists = [list(t) for t in set_of_tuples]

    return unique_list_of_lists

def main():
    list_of_lists = []

    try:
        n = int(input("Enter the number of lists: "))

        for element in range(n):
            
            user_input = input(f"Enter list {element + 1} (comma-separated values): ")
            # Convert the input string to a list of integers
            list_of_lists.append([int(value) for value in user_input.split(',')])

        print("\nOriginal list of lists:")
        print(list_of_lists)

        # Remove duplicates
        unique_list_of_lists = remove_duplicates(list_of_lists)

        print("\nList of lists after removing duplicates:")
        print(unique_list_of_lists)

    except ValueError as e:
        print(f"Invalid input: {e}")

if __name__ == "__main__":
    main()
