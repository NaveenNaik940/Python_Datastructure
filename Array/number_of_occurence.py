'''

@Author:Naveen Madev Naik
@Date: 2024-07-30 10:00:00
@Last Modified by: Naveen Madev Naik
@Last Modified time: 2024-07-30 10:00:00
@Title :program to get the number of occurrences of a specified element in an
        array.


'''


import array

def count_occurrences(arr, element):


    """
    Description:
        Count the number of occurrences of a specified element in the array.

    Parameters:
        arr (array.array): The array to search.
        element (int): The element to count in the array.

    Returns:
        int: The number of occurrences of the specified element.
    """


    return arr.count(element)

def main():
    try:
        user_input = input("Enter integers separated by spaces: ")
        int_list = [int(x) for x in user_input.split()]

        arr = array.array('i', int_list)

        print("\nArray items:")
        for item in arr:
            print(item, end=' ')
        print()

        element_to_count = int(input("Enter the element to count: "))

        count = count_occurrences(arr, element_to_count)

        print(f"\nThe element {element_to_count} occurs {count} times in the array.")

    except ValueError as e:
        print(f"Invalid input: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
