'''

@Author:Naveen Madev Naik
@Date: 2024-07-30 17:30:00
@Last Modified by: Naveen Madev Naik
@Last Modified time: 2024-07-30 17:30:00
@Title :program to check multiple keys exists in a dictionary.

'''


def check_keys_exist(my_dict, keys):


    """
    Description:
        Check if multiple keys exist in the given dictionary.

    Parameters:
        my_dict (dict): The dictionary to check.
        keys (list): The list of keys to check for existence.

    Returns:
        dict: A dictionary indicating which keys exist and which do not.
    """


    result = {}
    for key in keys:
        if key in my_dict:
            result[key] = True
        else:
            result[key] = False
    return result

def main():
    try:
        dict_input = input("Enter dictionary items as key=value pairs (comma-separated): ")
        dict_items = [item.strip() for item in dict_input.split(',')]

        my_dict = {}
        for item in dict_items:
            key, value = item.split('=')
            my_dict[key.strip()] = value.strip()

        print("\nDictionary created:")
        print(my_dict)

        keys_input = input("Enter the keys to check (comma-separated): ")
        keys_list = [key.strip() for key in keys_input.split(',')]

        existence = check_keys_exist(my_dict, keys_list)
        
        print("\nKey existence results:")
        for key, exists in existence.items():
            print(f"{key}: {'Exists' if exists else 'Does not exist'}")
    
    except ValueError as ve:
        print("Please enter key=value pairs correctly.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
