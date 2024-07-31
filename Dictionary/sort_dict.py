'''

@Author:Naveen Madev Naik
@Date: 2024-07-30 15:30:00
@Last Modified by: Naveen Madev Naik
@Last Modified time: 2024-07-30 15:30:00
@Title :script to sort (ascending and descending) a dictionary by
        value.

'''
    

def sort_dictionary_asc(my_dict):


    """
    Description:
        Sort a dictionary by its keys in ascending order.

    Parameters:
        my_dict (dict): The dictionary to be sorted.

    Returns:
        dict: A new dictionary sorted by keys in ascending order.
    """

    
    return dict(sorted(my_dict.items()))


def sort_dictionary_desc(my_dict):


    """
    Description:
        Sort a dictionary by its keys in descending order.

    Parameters:
        my_dict (dict): The dictionary to be sorted.

    Returns:
        dict: A new dictionary sorted by keys in descending order.
    """

    return dict(sorted(my_dict.items(), reverse=True))

def main():
    try:
        num_entries = int(input("Enter the number of entries you want to add to the dictionary: "))

        elements = []
        for _ in range(num_entries):
            key = input("Enter key: ")
            value = input("Enter value: ")
            elements.append((key, value))
        
        my_dict = {}
    
        for key, value in elements:
            my_dict[key] = value
        
        print("\nCreated dictionary:",my_dict)

        sorted_dict_asc= sort_dictionary_asc(my_dict)
        
        print("\nSorted dictionary (ascending order):", sorted_dict_asc)

        sorted_dict_desc=sort_dictionary_desc(my_dict)
        print("\nSorted dictionary (descending order):", sorted_dict_desc)

    except ValueError:
        print("Please enter a valid number.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
