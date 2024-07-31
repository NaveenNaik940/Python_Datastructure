'''

@Author:Naveen Madev Naik
@Date: 2024-07-30 10:00:00
@Last Modified by: Naveen Madev Naik
@Last Modified time: 2024-07-30 10:00:00
@Title :program to reverse the order of the items in the array.


'''


import array

def reverse_array(arr):


    """
    Description:
        Reverse the order of the items in the array.
    
    Parameters:
        arr (array.array): The original array.
    
    Returns:
        array.array: The array with its items reversed.
    """

    
    return arr[::-1]

def main():
    try:
        user_input = input("Enter integers separated by spaces: ")
        int_list = [int(x) for x in user_input.split()]
        
        arr = array.array('i', int_list)

        print("\nOriginal array items:")
        for item in arr:
            print(item, end=' ')
        print()

        reversed_arr = reverse_array(arr)

        print("\nReversed array items:")
        for item in reversed_arr:
            print(item, end=' ')
        print()

    except ValueError as e:
        print(f"Invalid input: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
