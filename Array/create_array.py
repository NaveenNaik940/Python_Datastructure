'''

@Author:Naveen Madev Naik
@Date: 2024-07-29 16:30:00
@Last Modified by: Naveen Madev Naik
@Last Modified time: 2024-07-29 16:30:00
@Title :program to create an array of 5 integers and display the array items.


'''


import array

def main():
    try:
        
        user_input = input("Enter 5 integers separated by spaces: ")
        int_list = [int(x) for x in user_input.split()]
        
        if len(int_list) != 5:
            raise ValueError("You must enter exactly 5 integers.")
        
        # Create an array of integers from the user input
        arr = array.array('i', int_list)

        # Display the array items
        print("\nArray items:")
        for item in arr:
            print(item, end=' ')
        print()

        print("\nAccessing individual elements:")
        for index in range(len(arr)):
            print(f"Element at index {index}: {arr[index]}")

    except ValueError as e:
        print(f"Invalid input: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
