'''

@Author:Naveen Madev Naik
@Date: 2024-07-30 11:40:00
@Last Modified by: Naveen Madev Naik
@Last Modified time: 2024-07-30 11:40:00
@Title :program to add member(s) in a set.

'''


def add_to_set(s, element):


    """
    Description:
        Add a single element to a set.

    Parameters:
        s (set): The set to add the element to.
        element: The element to add to the set.
    """

    s.add(element)
    return s

def update_set(s, elements):


    """
    Description:
        Add multiple elements to a set.

    Parameters:
        s (set): The set to add elements to.
        elements (iterable): The elements to add to the set.
    """


    s.update(elements)
    return s

def main():
    try:
        user_input = input("Enter initial set elements separated by spaces: ")
        elements = user_input.split()
        created_set = set(elements)
        
        new_element = input("Enter an element to add to the set: ")
        updated_set = add_to_set(created_set, new_element)
        
        print("\nSet after adding single element:")
        print(updated_set)
        
        new_elements = input("Enter multiple elements to add to the set, separated by spaces: ").split()
        updated_set = update_set(updated_set, new_elements)
        
        print("\nSet after adding multiple elements:")
        print(updated_set)
    
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()


