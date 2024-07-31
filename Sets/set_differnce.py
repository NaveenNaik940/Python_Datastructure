'''

@Author:Naveen Madev Naik
@Date: 2024-07-30 12:20:00
@Last Modified by: Naveen Madev Naik
@Last Modified time: 2024-07-30 12:20:00
@Title :program to create a diffrence of sets.

'''


def difference_of_sets(base_set, sets):


    """
    Description:
        Create the difference between the base set and multiple other sets.

    Parameters:
        base_set (set): The set from which to subtract.
        *sets: Other sets to subtract from the base set.

    Returns:
        set: The difference of the base set minus all other sets.
    """


    difference_result = base_set
    for item_set in sets:
        difference_result -= item_set
        
    return difference_result

def main():
    try:
        num_sets = int(input("Enter the number of sets (including base set): "))
        if num_sets < 1:
            raise ValueError("Number of sets must be at least 1.")

        all_sets = []

        for index in range(num_sets):
            user_input = input(f"Enter elements of set {index+1} separated by spaces: ")
            elements = user_input.split()
            all_sets.append(set(elements))

        base_set = all_sets[0]
        other_sets = all_sets[1:]
        
        difference_result = difference_of_sets(base_set, other_sets)
        
        print("\nDifference of the sets:")
        print(difference_result)
    
    except ValueError as e:
        print(f"Invalid input: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
