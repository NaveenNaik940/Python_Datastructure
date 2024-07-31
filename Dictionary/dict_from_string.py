'''

@Author:Naveen Madev Naik
@Date: 2024-07-30 17:10:00
@Last Modified by: Naveen Madev Naik
@Last Modified time: 2024-07-30 17:10:00
@Title :program to create a dictionary from a string.

'''


def create_dict_from_string(input_string):


    """
    Description:
        Create a dictionary from a string formatted as key:value pairs separated by commas.

    Parameters:
        input_string (str): The string to convert into a dictionary.

    Returns:
        dict: The resulting dictionary.
    """


    pairs = input_string.split(',')

    result_dict = {}
    for pair in pairs:
        key, value = pair.split(':')
        result_dict[key] = value
    
    return result_dict

def main():
    try:
        input_string = input("Enter the string formatted as key:value pairs separated by commas: ")

        result_dict = create_dict_from_string(input_string)
        
        print("\nCreated dictionary:", result_dict)
    
    except ValueError as ve:
        print("Error in input format. Make sure the string is formatted correctly as key:value pairs separated by commas.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
