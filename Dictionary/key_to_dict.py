'''

@Author:Naveen Madev Naik
@Date: 2024-07-30 15:30:00
@Last Modified by: Naveen Madev Naik
@Last Modified time: 2024-07-30 15:30:00
@Title :script to add a key to a dictionary.

'''
    

def add_key_to_dict(my_dict, key, value):


    """
    Description:
        Add a key-value pair to the dictionary.

    Parameters:
        my_dict (dict): The dictionary to be updated.
        key: The key to be added.
        value: The value to be added.

    Returns:
        None.
    """

    
    my_dict[key] = value


def main():
    try:
        my_dict = {'name': 'Alice', 'age': 30}
        print("Initial dictionary:", my_dict)

        key = input("Enter key to add: ")
        value = input("Enter value for the key: ")

        add_key_to_dict(my_dict, key, value)
        
        print("\nUpdated dictionary:", my_dict)
    
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
