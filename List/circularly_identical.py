'''

@Author:Naveen Madev Naik
@Date: 2024-07-29 14:40:00
@Last Modified by: Naveen Madev Naik
@Last Modified time: 2024-07-29 14:40:00
@Title :program to check whether two lists are circularly identical.

'''


def are_circularly_identical(list1, list2):
    """
    Dsecription:
        Check if two lists are circularly identical.

    Parameters:
        list1 (list): The first list.
        list2 (list): The second list.

    Returns:
        bool: True if the lists are circularly identical, False otherwise.
    """
    if len(list1) != len(list2):
        return False

    concatenated = list1 + list1

    for i in range(len(list1)):
        if concatenated[i:i+len(list2)] == list2:
            return True

    return False

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
        if are_circularly_identical(list1, list2):
            print("The lists are circularly identical.")
        else:
            print("The lists are not circularly identical.")

    except ValueError as e:
        print(f"{e}")    

if __name__ == "__main__":
    main()
