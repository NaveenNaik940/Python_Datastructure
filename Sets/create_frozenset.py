'''

@Author:Naveen Madev Naik
@Date: 2024-07-30 12:30:00
@Last Modified by: Naveen Madev Naik
@Last Modified time: 2024-07-30 12:30:00
@Title :program to use of frozensets.

'''


def create_frozenset(elements):


    """
    Description:
        Create a frozenset from a list of elements.

    Parameters:
        elements (list): List of elements to include in the frozenset.

    Returns:
        frozenset: The created frozenset.
    """


    return frozenset(elements)

def main():
    try:
        user_input = input("Enter elements for the frozenset, separated by spaces: ")
        elements = user_input.split()

        my_frozenset = create_frozenset(elements)
        
        print("\nOriginal frozenset:", my_frozenset)

        print("\nLength of the frozenset:", len(my_frozenset))

        print("\nIterating over frozenset:")
        for item in my_frozenset:
            print(item)
    
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
