'''

@Author:Naveen Madev Naik
@Date: 2024-07-30 11:20:00
@Last Modified by: Naveen Madev Naik
@Last Modified time: 2024-07-30 11:20:00
@Title :program to check whether an element exists within a tuple.


'''


def element_exists(t, element):


    """
    Description:
        Check if a specific element exists in a tuple.

    Parameters:
        t (tuple): The tuple to check.
        element (int): The integer element to check for.

    Returns:
        bool: True if the element exists in the tuple, False otherwise.
    """


    return element in t

def main():
    try:
        user_input = input("Enter integer tuple elements separated by spaces: ")
        
        elements = user_input.split()
        
        elements = [int(element) for element in elements]
        
        created_tuple = tuple(elements)
        
        check_element = int(input("Enter the integer to check for: "))

        exists = element_exists(created_tuple, check_element)
        
        if exists:
            print(f"\nElement {check_element} exists in the tuple.")
        else:
            print(f"\nElement {check_element} does not exist in the tuple.")
    
    except ValueError:
        print("Invalid input. Please enter valid integers.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
