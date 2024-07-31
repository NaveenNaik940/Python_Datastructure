'''

@Author:Naveen Madev Naik
@Date: 2024-07-30 17:40:00
@Last Modified by: Naveen Madev Naik
@Last Modified time: 2024-07-30 17:40:00
@Title :program to count number of items in a dictionary value
        that is a list.

'''


def count_items_in_list_values(my_dict):


    """
    Description:
        Count the total number of items in the values of the dictionary where the values are lists.

    Parameters:
        my_dict (dict): The dictionary with list values.

    Returns:
        int: The total number of items in all lists.
    """


    total_count = 0
    for value in my_dict.values():
        if isinstance(value, list): 
            total_count += len(value)  
    return total_count

def main():
    try:
        dict_input = input("Enter dictionary items as key=[value1,value2,...] pairs (comma-separated): ")
        dict_items = [item.strip() for item in dict_input.split(',')]

        my_dict = {}
        for item in dict_items:
            key, values = item.split('=')
            value_list = values.strip('[]').split(',')
            value_list = [value.strip() for value in value_list] 
            my_dict[key.strip()] = value_list

        print("\nDictionary created:")
        print(my_dict)

        total_items = count_items_in_list_values(my_dict)
        
        print(f"\nTotal number of items in list values: {total_items}")
    
    except ValueError as ve:
        print("Please enter key=[value1,value2,...] pairs correctly.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
