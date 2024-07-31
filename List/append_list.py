'''

@Author:Naveen Madev Naik
@Date: 2024-07-29 14:24:00
@Last Modified by: Naveen Madev Naik
@Last Modified time: 2024-07-29 14:24:00
@Title :program to append a list to the second list.

'''


def append_list(list1, list2):


    """
    Description:
        append the list2 to list1.

    Parameters:
        list1 (list): The first list.
        list2 (list): The second list.

    Returns:
        list: list contains appended list2 to list1
    """
    list1.extend(list2)
    
    return list1

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
        
        print("after appending list2 to list1:", append_list(list1,list2))

    except ValueError as e:
        print(e)    

if __name__ == "__main__":
    main()