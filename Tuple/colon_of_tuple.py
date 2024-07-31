'''

@Author:Naveen Madev Naik
@Date: 2024-07-30 11:00:00
@Last Modified by: Naveen Madev Naik
@Last Modified time: 2024-07-30 11:00:00
@Title :program to create the colon of a tuple.


'''


def create_colon_tuple(start_value, end_value, step):


    """
    Description:
        Create a tuple representing a range using colon notation.

    Parameters:
        start_value (int): The start value of the range.
        end_value (int): The end value of the range.
        step (int): The step value of the range.

    Returns:
        tuple: The created tuple representing the range.
    """

    
    return tuple(range(start_value, end_value, step))

def main():
    try:
        start_value = int(input("Enter the start value: "))
        end_value = int(input("Enter the end value: "))
        step = int(input("Enter the step value: "))

        colon_tuple = create_colon_tuple(start_value, end_value, step)

        print("\nTuple representing the range:")
        print(colon_tuple)

    except ValueError:
        print("Please enter valid integers for the start, end, and step values.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
