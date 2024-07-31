'''

@Author:Naveen Madev Naik
@Date: 2024-07-30 17:10:00
@Last Modified by: Naveen Madev Naik
@Last Modified time: 2024-07-30 17:10:00
@Title :program to print a dictionary in table format.

'''

def print_dict_table(my_dict):


    """
    Description:
        Print the dictionary in table format without external libraries.

    Parameters:
        my_dict (dict): The dictionary to print.

    Returns:
        None
    """


    max_key_len = max(len(str(key)) for key in my_dict.keys())
    max_value_len = max(len(str(value)) for value in my_dict.values())
    
    print(f"{'Key':<{max_key_len}} | {'Value':<{max_value_len}}")
    print("-" * (max_key_len + max_value_len + 3))
    
    for key, value in my_dict.items():
        print(f"{key:<{max_key_len}} | {value:<{max_value_len}}")

def main():
    try:
        num_entries = int(input("Enter the number of entries for the dictionary: "))
        my_dict = {}
        
        for _ in range(num_entries):
            key = input("Enter key: ")
            value = input("Enter value: ")
            my_dict[key] = value
        print_dict_table(my_dict)
    
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
