'''

@Author:Naveen Madev Naik
@Date: 2024-07-30 17:00:00
@Last Modified by: Naveen Madev Naik
@Last Modified time: 2024-07-30 17:00:00
@Title :program to print all unique values in a dictionary.

'''


def print_unique_values(dict_list):


    """
    Description:
        Print all unique values from a list of dictionaries.

    Parameters:
        dict_list (list): List of dictionaries containing values.

    Returns:
        None
    """


    unique_values = set()
    
    for item_dict in dict_list:
        for value in item_dict.values():
            unique_values.add(value)
    
    print("Unique values:", unique_values)

def create_dictionary_from_input():


    """
    Description:
        Create a dictionary from user input.

    Returns:
        dict: The created dictionary with user input key-value pairs.
    """


    num_entries = int(input("Enter the number of entries for this dictionary: "))
    my_dict = {}
    
    for _ in range(num_entries):
        key = input("Enter key: ")
        value = input("Enter value: ")
        my_dict[key] = value
    
    return my_dict

def main():
    try:
        num_dicts = int(input("Enter the number of dictionaries: "))
        dict_list = []
        
        for i in range(num_dicts):
            print(f"\nEnter entries for dictionary {i+1}:")
            dict_list.append(create_dictionary_from_input())
        
        print("\nList of dictionaries:")
        for item_dict in dict_list:
            print(item_dict)
        
        print("\nExtracting unique values...")
        print_unique_values(dict_list)
    
    except ValueError:
        print("Please enter a valid number.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
