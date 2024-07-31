'''

@Author:Naveen Madev Naik
@Date: 2024-07-29 14:24:00
@Last Modified by: Naveen Madev Naik
@Last Modified time: 2024-07-29 14:24:00
@Title :program to generate all permutations of a list in Python.

'''


import itertools

def generate_permutations(input_list):


    """
    Description:
        Generate all permutations of the given list.

    Parameters:
        input_list: The list of elements to permute.

    Returns:
        list of tuples: A list containing all permutations of the input list.
    """


    permutations = list(itertools.permutations(input_list))
    
    return permutations

def main():
    try:
        no_of_element= int(input("Enter the number of element in the original list: "))
        normal_list=[]
        print("enter the integer element in the list one by one")
        for element in range(no_of_element):
            normal_list.append(int(input(": ")))
        all_permutations = generate_permutations(normal_list)
    
        print("All permutations:")
        for perm in all_permutations:
            print(list(perm))

    except ValueError as e:
        print(e)        

if __name__ == "__main__":
    main()
