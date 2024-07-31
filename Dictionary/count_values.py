'''

@Author:Naveen Madev Naik
@Date: 2024-07-30 17:10:00
@Last Modified by: Naveen Madev Naik
@Last Modified time: 2024-07-30 17:10:00
@Title :program to count the values associated with key in a
        dictionary.

'''


from collections import Counter

def count_values(my_dict, key):


    """
    Description:
        Count the occurrences of each value associated with a given key in the dictionary.

    Parameters:
        my_dict (dict): The dictionary containing key-value pairs.
        key: The key for which the values need to be counted.

    Returns:
        dict: A dictionary with values as keys and their counts as values.
    """


    if key not in my_dict:
        print(f"Key '{key}' not found in the dictionary.")
        return {}

    values = my_dict[key]

    value_counts = Counter(values)
    
    return value_counts

def create_dictionary_from_input():


    """
    Description:
        Create a dictionary from user input.
    
    Parameter:
        None

    Returns:
        dict: The created dictionary with user input key-value pairs.
    """


    num_entries = int(input("Enter the number of key-value pairs for the dictionary: "))
    my_dict = {}
    
    for _ in range(num_entries):
        key = input("Enter key: ")
        values_input = input("Enter values (comma-separated): ")
        values = values_input.split(',')
        values = [value.strip() for value in values] 
        my_dict[key] = values
    
    return my_dict

def main():
    try:
        print("Enter the dictionary details:")
        my_dict = create_dictionary_from_input()
        
        print("\nDictionary created:")
        for key, value in my_dict.items():
            print(f"{key}: {value}")

        key = input("\nEnter the key to count values for: ")

        counts = count_values(my_dict, key)
        
        if counts:
            print("\nValue counts:")
            for value, count in counts.items():
                print(f"{value}: {count}")
    
    except ValueError as ve:
        print("Please enter a valid number.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
