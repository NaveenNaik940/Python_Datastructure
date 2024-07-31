'''

@Author:Naveen Madev Naik
@Date: 2024-07-30 12:00:00
@Last Modified by: Naveen Madev Naik
@Last Modified time: 2024-07-30 12:00:00
@Title :program to create an intersection of sets.

'''

def intersect_sets(sets):


    """
    Description:
        Create the intersection of multiple sets.

    Parameters:
        sets: Multiple sets to intersect.

    Returns:
        set: The intersection of all the provided sets.
    """


    if not sets:
        return set()
    
    intersection_result = sets[0]
    for item_set in sets[1:]:
        intersection_result &= item_set
        
    return intersection_result

def main():
    try:
        num_sets = int(input("Enter the number of sets: "))
        all_sets = []

        for index in range(num_sets):
            user_input = input(f"Enter elements of set {index+1} separated by spaces: ")
            elements = user_input.split()
            all_sets.append(set(elements))

        # Find the intersection of all sets
        intersection_result = intersect_sets(all_sets)
        
        print("\nIntersection of all sets:")
        print(intersection_result)
    
    except ValueError as e:
        print("Invalid input. Please enter numeric values where expected.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
