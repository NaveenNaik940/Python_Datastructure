'''

@Author:Naveen Madev Naik
@Date: 2024-07-30 10:30:00
@Last Modified by: Naveen Madev Naik
@Last Modified time: 2024-07-30 10:30:00
@Title :program to unpack a tuple in several variables.


'''


def create_mixed_tuple(elements):
    """
    Description:
        Create a tuple with different data types from a list of elements.

    Parameters:
        elements (list): The list of elements to convert and pack into a tuple.

    Returns:
        tuple: The created tuple with mixed data types.
    """
    try:
        mixed_elements = []
        for element in elements:
            if element.isdigit():
                mixed_elements.append(int(element))
            elif element.replace('.', '', 1).isdigit() and element.count('.') < 2:
                mixed_elements.append(float(element))
            elif element.lower() == 'true':
                mixed_elements.append(True)
            elif element.lower() == 'false':
                mixed_elements.append(False)
            else:
                mixed_elements.append(element)
        
        created_tuple = tuple(mixed_elements)
        
        return created_tuple

    except Exception as e:
        print(f"An error occurred: {e}")
        return ()

def unpack_tuple(t):
    """
    Description:
        Unpack the elements of a tuple into individual variables.

    Parameters:
        t (tuple): The tuple to unpack.

    Returns:
        list: The list of individual variables.
    """
    return list(t)

def main():
    try:
        user_input = input(f"Enter values separated by spaces: ")
        elements = user_input.split()
    
        created_tuple = create_mixed_tuple(elements)

        if created_tuple:
            print("\nOriginal tuple:")
            print(created_tuple)

            unpacked_values = unpack_tuple(created_tuple)

            print("\nUnpacked variables:")
            for idx, value in enumerate(unpacked_values):
                print(f"Element id_{idx + 1} = {value}")

    except ValueError:
        print("Please enter a valid integer for the number of elements.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
