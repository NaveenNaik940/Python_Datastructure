'''

@Author:Naveen Madev Naik
@Date: 2024-07-30 17:30:00
@Last Modified by: Naveen Madev Naik
@Last Modified time: 2024-07-30 17:30:00
@Title :program to convert a list into a nested dictionary of keys.

'''

def list_to_nested_dict(lst):


    """
    Description:
        Convert a list into a nested dictionary of keys.

    Parameters:
        lst (list): The list to convert into a nested dictionary.

    Returns:
        dict: The resulting nested dictionary.
    """


    if not lst:
        return {}

    nested_dict = {}
    current_level = nested_dict

    for item in lst:
        current_level[item] = {}
        current_level = current_level[item]
    
    return nested_dict

def main():
    try:
        user_input = input("Enter a list of keys separated by commas: ")

        keys_list = [key.strip() for key in user_input.split(',')]

        nested_dict = list_to_nested_dict(keys_list)
        
        print("\nNested dictionary:")
        print(nested_dict)
    
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
