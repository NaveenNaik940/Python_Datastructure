'''

@Author:Naveen Madev Naik
@Date: 2024-07-29 14:24:00
@Last Modified by: Naveen Madev Naik
@Last Modified time: 2024-07-29 14:24:00
@Title :program to get the difference between the two lists.

'''


def list_difference(list1, list2):


    """
    Description:
        Find items that are in list1 but not in list2.

    Parameters:
        list1 (list): The first list.
        list2 (list): The second list.

    Returns:
        list: A list containing items in list1 but not in list2.
    """

    
    return [item for item in list1 if item not in list2]

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
        diff = list_difference(list1, list2)
        
        print("Difference between list1 and list2:", diff)

    except ValueError as e:
        print(e)    

if __name__ == "__main__":
    main()