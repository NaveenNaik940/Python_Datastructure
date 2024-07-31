'''

@Author:Naveen Madev Naik
@Date: 2024-07-30 10:00:00
@Last Modified by: Naveen Madev Naik
@Last Modified time: 2024-07-30 10:00:00
@Title :program to create a tuple.


'''


def main():
    try:
        user_input = input("Enter elements separated by spaces: ")
        
        elements = user_input.split()
        
        elements = [int(element) for element in user_input.split()]
        created_tuple = tuple(elements)
        
        print("\nCreated tuple:")
        print(created_tuple)

    except Exception as e:
        print(f"An error occurred: {e}")
       

if __name__ == "__main__":
    main()
