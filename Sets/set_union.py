'''

@Author:Naveen Madev Naik
@Date: 2024-07-30 12:20:00
@Last Modified by: Naveen Madev Naik
@Last Modified time: 2024-07-30 12:20:00
@Title :program to create a union of sets.

'''


def union_of_sets(sets):


    """
    Description:
        Create the union of multiple sets.

    Parameters:
        sets: Multiple sets to unite.

    Returns:
        set: The union of all the provided sets.
    """


    if not sets:
        return set()
    
    union_result = sets[0]
    for item_set in sets[1:]:
        union_result |= item_set
        
    return union_result

def main():
    try:
        num_sets = int(input("Enter the number of sets: "))
        all_sets = []

        for i in range(num_sets):
            user_input = input(f"Enter elements of set {i+1} separated by spaces: ")
            elements = user_input.split()
            all_sets.append(set(elements))

        union_result = union_of_sets(all_sets)
        
        print("\nUnion of all sets:")
        print(union_result)
    
    except ValueError as e:
        print("Invalid input. Please enter numeric values where expected.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
