'''

@Author:Naveen Madev Naik
@Date: 2024-07-30 10:00:00
@Last Modified by: Naveen Madev Naik
@Last Modified time: 2024-07-30 10:00:00
@Title :program to remove the first occurrence of a specified element from an
        array.


'''


import array

def remove_first_occurrence(arr, element):


    """
    Description:
        Remove the first occurrence of a specified element from the array.

    Parameters:
        arr (array.array): The array to modify.
        element (int): The element to remove from the array.

    Returns:
        array.array: The modified array.
    """


    try:
        arr.remove(element)
    except ValueError:
        print(f"The element {element} is not found in the array.")
    return arr

def main():
    try:
        user_input = input("Enter integers separated by spaces: ")
        int_list = [int(x) for x in user_input.split()]

        arr = array.array('i', int_list)

        print("\nOriginal array items:")
        for item in arr:
            print(item, end=' ')
        print()

        element_to_remove = int(input("Enter the element to remove: "))
        
        arr = remove_first_occurrence(arr, element_to_remove)

        print("\nArray items after removing the first occurrence of the element:")
        for item in arr:
            print(item, end=' ')
        print()

    except ValueError as e:
        print(f"Invalid input: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
