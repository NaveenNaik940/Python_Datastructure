'''

@Author:Naveen Madev Naik
@Date: 2024-07-30 16:30:00
@Last Modified by: Naveen Madev Naik
@Last Modified time: 2024-07-30 16:30:00
@Title :program to iterate over dictionaries using for loops.

'''

def iterate_dictionary(my_dict):


    """
    Description:
        Iterate over a dictionary and print its key-value pairs.

    Parameters:
        my_dict (dict): The dictionary to iterate over.

    Returns:
        None
    """


    for key, value in my_dict.items():
        print(f"Key: {key}, Value: {value}")

def main():
    try:
        num_entries = int(input("Enter the number of entries for the dictionary: "))
        my_dict = {}
        
        for _ in range(num_entries):
            key = input("Enter key: ")
            value = input("Enter value: ")
            my_dict[key] = value

        print("\nIterating over the dictionary:")
        iterate_dictionary(my_dict)
    
    except ValueError:
        print("Please enter a valid number.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
