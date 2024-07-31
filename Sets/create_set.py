'''

@Author:Naveen Madev Naik
@Date: 2024-07-30 11:40:00
@Last Modified by: Naveen Madev Naik
@Last Modified time: 2024-07-30 11:40:00
@Title :program to create a set.


'''


def create_set(elements):


    """
    Description:
        Create a set from a list of elements.

    Parameters:
        elements (list): The list of elements to convert to a set.

    Returns:
        set: The created set.
    """


    return set(elements)

def main():
    try:
        user_input = input("Enter set elements separated by spaces: ")

        elements = user_input.split()

        created_set = create_set(elements)

        print("\nCreated set:")
        print(created_set)
    
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
