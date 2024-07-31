'''

@Author:Naveen Madev Naik
@Date: 2024-07-30 14:00:00
@Last Modified by: Naveen Madev Naik
@Last Modified time: 2024-07-30 14:00:00
@Title :program to find maximum and the minimum value in a set.

'''


def find_max_min(given_set):


    """
    Description:
        Find the maximum and minimum values in a set.

    Parameters:
        given_set(set): The set to find max and min values in.

    Returns:
        tuple: A tuple containing the maximum and minimum values.
    """


    if not given_set:
        return None, None

    max_value = max(given_set)
    min_value = min(given_set)
    
    return max_value, min_value

def main():
    try:
        user_input = input("Enter elements for the set, separated by spaces: ")
        elements = user_input.split()

        elements = [int(element) for element in elements]

        my_set = set(elements)
        
        print("\nOriginal set:", my_set)

        max_value, min_value = find_max_min(my_set)
        
        if max_value is None and min_value is None:
            print("The set is empty. No max or min values.")
        else:
            print(f"Maximum value in the set: {max_value}")
            print(f"Minimum value in the set: {min_value}")
    
    except ValueError:
        print("Please enter valid integers only.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
