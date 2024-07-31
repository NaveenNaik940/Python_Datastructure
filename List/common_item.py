'''

@Author:Naveen Madev Naik
@Date: 2024-07-29 16:00:00
@Last Modified by: Naveen Madev Naik
@Last Modified time: 2024-07-29 16:00:00
@Title :program to find common items from two lists.

'''


def common_items(list1, list2):


    """
    Description:
        Find common items between two lists using list comprehension.

    Parameters:
        list1 (list): The first list.
        list2 (list): The second list.

    Returns:
        list: A list containing the common items.
    """


    return [item for item in list1 if item in list2]

def main():
    try:
        no_of_element1=int(input("enter the number of element you want to add in list1: "))
        list1 = []
        print("enter the element in list1")
        for index in range(no_of_element1):
            list1.append(int(input(": ")))
        no_of_element2=int(input("enter the number of element you want to add in list2: "))
        list2 = []
        print("enter the element in list2")
        for index in range(no_of_element2):
            list2.append(int(input(": ")))

        common = common_items(list1, list2)
        print("Common items:", common)

    except ValueError as e:
        print(f"{e}")    

if __name__ == "__main__":
    main()


