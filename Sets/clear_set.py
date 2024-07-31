'''

@Author:Naveen Madev Naik
@Date: 2024-07-30 12:30:00
@Last Modified by: Naveen Madev Naik
@Last Modified time: 2024-07-30 12:30:00
@Title :program to clear a set.

'''


def clear_set(given_set):


    """
    Description:
        Clear all elements from the set.

    Parameters:
        given_set (set): The set to be cleared.

    Returns:
        None
    """

    given_set.clear()

def main():
    try:
        user_input = input("Enter elements of the set separated by spaces: ")
        elements = user_input.split()
        my_set = set(elements)

        print("\nOriginal set:")
        print(my_set)

        clear_set(my_set)
        
        print("\nSet after clearing:")
        print(my_set)
    
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
