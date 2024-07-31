'''

@Author:Naveen Madev Naik
@Date: 2024-07-30 12:30:00
@Last Modified by: Naveen Madev Naik
@Last Modified time: 2024-07-30 12:30:00
@Title :program to create a symmetric diffrence of sets.

'''


def symmetric_difference_of_sets(sets):


    """
    Description:
        Create the symmetric difference of multiple sets.

    Parameters:
        sets: Multiple sets to compute the symmetric difference.

    Returns:
        set: The symmetric difference of all the provided sets.
    """

    if not sets:
        return set()
    
    symmetric_diff_result = sets[0]
    for item_set in sets[1:]:
        symmetric_diff_result ^= item_set
        
    return symmetric_diff_result

def main():
    try:
        num_sets = int(input("Enter the number of sets: "))
        if num_sets < 1:
            raise ValueError("Number of sets must be at least 1.")

        all_sets = []

        for i in range(num_sets):
            user_input = input(f"Enter elements of set {i+1} separated by spaces: ")
            elements = user_input.split()
            all_sets.append(set(elements))

        symmetric_diff_result = symmetric_difference_of_sets(*all_sets)
        
        print("\nSymmetric difference of the sets:")
        print(symmetric_diff_result)
    
    except ValueError as e:
        print(f"Invalid input: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
