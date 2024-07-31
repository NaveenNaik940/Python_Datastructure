'''

@Author:Naveen Madev Naik
@Date: 2024-07-30 16:30:00
@Last Modified by: Naveen Madev Naik
@Last Modified time: 2024-07-30 16:30:00
@Title :program to remove a key from a dictionary.

'''


def remove_key(my_dict, key_to_remove):


    """
    Description:
        Remove a specified key from the dictionary if it exists.

    Parameters:
        my_dict (dict): The dictionary from which the key is to be removed.
        key_to_remove: The key to remove from the dictionary.

    Returns:
        dict: The updated dictionary.
    """


    if key_to_remove in my_dict:
        del my_dict[key_to_remove]
    else:
        print(f"Key '{key_to_remove}' not found in the dictionary.")
    return my_dict

def main():
    try:
        num_entries = int(input("Enter the number of entries for the dictionary: "))
        my_dict = {}
        
        for _ in range(num_entries):
            key = input("Enter key: ")
            value = input("Enter value: ")
            my_dict[key] = value
        
        print("\nOriginal dictionary:", my_dict)

        key_to_remove = input("Enter the key to remove: ")

        updated_dict = remove_key(my_dict, key_to_remove)
        
        print("\nUpdated dictionary:", updated_dict)
    
    except ValueError:
        print("Please enter a valid number.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
