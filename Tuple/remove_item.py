'''

@Author:Naveen Madev Naik
@Date: 2024-07-30 11:20:00
@Last Modified by: Naveen Madev Naik
@Last Modified time: 2024-07-30 11:20:00
@Title :program to remove an item from a tuple.


'''


def remove_item(t, item_to_remove):


    """
    Description:
        Remove a specific item from a tuple and return a new tuple.

    Parameters:
        t (tuple): The original tuple.
        item_to_remove: The item to remove from the tuple.

    Returns:
        tuple: A new tuple with the specified item removed.
    """


    new_tuple = tuple(item for item in t if item != item_to_remove)
    return new_tuple

def main():
    try:
        user_input = input("Enter tuple elements separated by spaces: ")

        elements = user_input.split()

        elements = [int(element) for element in elements]

        created_tuple = tuple(elements)
        
        item_to_remove = int(input("Enter the integer item to remove: "))

        updated_tuple = remove_item(created_tuple, item_to_remove)
        
        print("\nUpdated tuple after removal:")
        print(updated_tuple)
    
    except ValueError:
        print("Invalid input. Please enter valid integers.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
