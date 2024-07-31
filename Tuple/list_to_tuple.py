'''

@Author:Naveen Madev Naik
@Date: 2024-07-30 11:20:00
@Last Modified by: Naveen Madev Naik
@Last Modified time: 2024-07-30 11:20:00
@Title :program to create the colon of a tuple.


'''


def list_to_tuple(lst):
    """
    Description:
        Convert a list to a tuple.

    Parameters:
        lst (list): The list to convert.

    Returns:
        tuple: The converted tuple.
    """
    return tuple(lst)

def main():
    try:
        user_input = input("Enter list elements separated by spaces: ")

        elements = user_input.split()

        elements = [int(element) for element in elements]

        converted_tuple = list_to_tuple(elements)

        print("\nConverted tuple:")
        print(converted_tuple)
    
    except ValueError:
        print("Invalid input. Please enter valid integers.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
