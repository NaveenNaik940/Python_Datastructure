'''

@Author:Naveen Madev Naik
@Date: 2024-07-29 12:44:00
@Last Modified by: Naveen Madev Naik
@Last Modified time: 2024-07-29 12:44:00
@Title :function that takes two lists and returns True if they have at
        least one common member.

'''


def is_list_contain_one_member(original_list, compare_list):


    """
    Description:
        returns true if compare list conatins atleast one member in original list
    
    Parameters:
        original_list : original list which will get compared to compare_list.
        compare_list : will check whether this list contains atleast one member in original_list
    
    Returns:
        Boolean:True or False
    """



    return False
   

def main():
    
    try:
        no_of_element1 = int(input("Enter the number of element in the original list: "))
        original_list=[]
        print("enter the element in the list one by one")
        for element in range(no_of_element1):
            original_list.append(input(": "))

        no_of_element2 = int(input("Enter the number of element in the compare list: "))
        compare_list=[]
        print("enter the element in the list one by one")
        for element in range(no_of_element1):
            compare_list.append(input(": "))    
        if is_list_contain_one_member(original_list,compare_list):
            print("yes it contains element")
        else:
            print("No its does not contain element")    
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
