'''

@Author:Naveen Madev Naik
@Date: 2024-07-30 16:30:00
@Last Modified by: Naveen Madev Naik
@Last Modified time: 2024-07-30 16:30:00
@Title :script to concatenate following dictionaries to create a new
        one.

'''


def concatenate_dictionaries(dicts):


    """
    Concatenate multiple dictionaries into a new one.

    Parameters:
        *dicts: Variable number of dictionary arguments.

    Returns:
        dict: The concatenated dictionary.
    """


    concatenated_dict = {}
    for dict_item in dicts:
        concatenated_dict.update(dict_item)
    return concatenated_dict


def main():
    try:
        num_dicts = int(input("Enter the number of dictionaries you want to concatenate: "))
        
        my_dict = {}
        dictionary=[]
        for index in range(num_dicts):
            print(f"\nEnter entries for dictionary {index+1}:")
            num_entries = int(input("Enter the number of entries for this dictionary: "))
            for _ in range(num_entries):
                key = input("Enter key: ")
                value = input("Enter value: ")
                my_dict[key] = value
            print(f"dictionary {index}: {my_dict}")    
            dictionary.append(my_dict)
            my_dict={}
            print(dictionary)
            
        concatenated_dict = concatenate_dictionaries(dictionary)
        
        print("\nConcatenated dictionary:", concatenated_dict)
    
    except ValueError:
        print("Please enter a valid number.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
