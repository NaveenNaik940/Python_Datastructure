'''

@Author:Naveen Madev Naik
@Date: 2024-07-30 11:40:00
@Last Modified by: Naveen Madev Naik
@Last Modified time: 2024-07-30 11:40:00
@Title :program to remove element in a set.

'''


def remove_from_set(given_set, item):


    """
    Description:
        Remove an item from a set.

    Parameters:
        given_set (set): The set from which to remove the item.
        item: The item to remove from the set.

    Returns:
        set: The updated set with the item removed.
    """

    given_set.discard(item)  
    return given_set

def main():
    try:
        user_input = input("Enter initial set elements separated by spaces: ")
        elements = user_input.split()
        created_set = set(elements)
        
        item_to_remove = input("Enter an element to remove from the set: ")
        updated_set = remove_from_set(created_set, item_to_remove)
        
        print("\nSet after removing the element:")
        print(updated_set)
    
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
