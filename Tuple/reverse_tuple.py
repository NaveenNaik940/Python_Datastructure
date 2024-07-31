'''

@Author:Naveen Madev Naik
@Date: 2024-07-30 11:20:00
@Last Modified by: Naveen Madev Naik
@Last Modified time: 2024-07-30 11:20:00
@Title :program to reverse a tuple.


'''


def reverse_tuple(t):


    """
    Description:
        Reverse a tuple.

    Parameters:
        t (tuple): The tuple to reverse.

    Returns:
        tuple: The reversed tuple.
    """


    return t[::-1]

def main():
    try:
        user_input = input("Enter tuple elements separated by spaces: ")

        elements = user_input.split()

        elements = [int(element) for element in elements]

        created_tuple = tuple(elements)

        reversed_tuple = reverse_tuple(created_tuple)

        print("\nReversed tuple:")
        print(reversed_tuple)
    
    except ValueError:
        print("Invalid input. Please enter valid integers.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
