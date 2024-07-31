'''

@Author:Naveen Madev Naik
@Date: 2024-07-29 13:24:00
@Last Modified by: Naveen Madev Naik
@Last Modified time: 2024-07-29 13:24:00
@Title :program to print a specified list after removing the 0th, 4th and
        5th elements.

'''


def remove_specified_element(original_list):


    """
    Description:
        returns list after removing 0th, 4th and 5th element
    
    Parameters:
        original_list : will remove 0th ,4th and 5th element from original list.
        
    Returns:
        list
    """


    original_list.pop(5)
    original_list.pop(4)
    original_list.pop(0)
    return original_list
   

def main():
    
    try:
        no_of_element1 = int(input("Enter the number of element in the original list which should be greater than 5: "))
        if no_of_element1<5:
            raise ValueError("number should be equal or greater than ")
        original_list=[]
        print("enter the element in the list one by one")
        for element in range(no_of_element1):
            original_list.append(input(": "))
        print(f"after removing the 0th, 4th and 5th element from {original_list} is : {remove_specified_element(original_list)}")   
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
