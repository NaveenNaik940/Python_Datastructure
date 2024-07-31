'''

@Author:Naveen Madev Naik
@Date: 2024-07-30 11:20:00
@Last Modified by: Naveen Madev Naik
@Last Modified time: 2024-07-30 11:20:00
@Title :program to slice a tuple.


'''


def slice_tuple(t, start, end, step):


    """
    Description:
        Slice a tuple based on the given indices and step.

    Parameters:
        t (tuple): The tuple to slice.
        start (int): The start index for slicing.
        end (int): The end index for slicing.
        step (int): The step for slicing.

    Returns:
        tuple: The sliced portion of the tuple.
    """


    return t[start:end:step]

def main():
    try:
        user_input = input("Enter tuple elements separated by spaces: ")

        elements = user_input.split()

        elements = [int(element) for element in elements]

        created_tuple = tuple(elements)

        start = int(input("Enter the start index for slicing: "))
        end = int(input("Enter the end index for slicing: "))
        step = int(input("Enter the step for slicing: "))

        sliced_tuple = slice_tuple(created_tuple, start, end, step)

        print("\nSliced tuple:")
        print(sliced_tuple)
    
    except ValueError:
        print("Invalid input. Please enter valid integers.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()

