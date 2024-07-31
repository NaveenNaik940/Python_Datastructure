'''

@Author:Naveen Madev Naik
@Date: 2024-07-30 11:40:00
@Last Modified by: Naveen Madev Naik
@Last Modified time: 2024-07-30 11:40:00
@Title :program to iterate over a set.


'''


def iterate_set(s):


    """
    Description:
        Iterate over a set and print each element.

    Parameters:
        s (set): The set to iterate over.
    """

    
    print("Iterating over the set:")
    for item in s:
        print(item)

def main():
    try:
        user_input = input("Enter set elements separated by spaces: ")

        elements = user_input.split()

        created_set = set(elements)

        iterate_set(created_set)
    
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
