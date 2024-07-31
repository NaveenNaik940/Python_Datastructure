'''

@Author:Naveen Madev Naik
@Date: 2024-07-30 11:20:00
@Last Modified by: Naveen Madev Naik
@Last Modified time: 2024-07-30 11:20:00
@Title :program to find the repeated items of a tuple.


'''


def find_repeated_items(t):


    """
    Description:
        Find the repeated items in a tuple.

    Parameters:
        t (tuple): The tuple to check for repeated items.

    Returns:
        list: A list of repeated items.
    """

    count_dict = {}
    
    for item in t:
        if item in count_dict:
            count_dict[item] += 1
        else:
            count_dict[item] = 1
    
    repeated_items = [item for item, count in count_dict.items() if count > 1]
    
    return repeated_items

def main():
    try:
        user_input = input("Enter tuple elements separated by spaces: ")
 
        elements = user_input.split()
        
        mixed_elements = []
        for element in elements:
            if element.isdigit():
                mixed_elements.append(int(element))
            elif element.replace('.', '', 1).isdigit() and element.count('.') < 2:
                mixed_elements.append(float(element))
            elif element.lower() == 'true':
                mixed_elements.append(True)
            elif element.lower() == 'false':
                mixed_elements.append(False)
            else:
                mixed_elements.append(element)

        created_tuple = tuple(mixed_elements)
        
        repeated_items = find_repeated_items(created_tuple)
        
        if repeated_items:
            print("\nRepeated items:")
            print(repeated_items)
        else:
            print("\nNo repeated items found.")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
