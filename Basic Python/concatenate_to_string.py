'''

@Author:Naveen Madev Naik
@Date: 2024-07-26 12:00:00
@Last Modified by: Naveen Madev Naik
@Last Modified time: 2024-07-26 12:00:00
@Title :program to concatenate all elements in a list into a string and return it.

'''


def concatenate_to_str(element_list):
    

    """
    Description:
        function will return the concatenated string
    Parameter:
        element_list: element in the list will be concatenated
    return:
        String        
    """
    
    concatenated_string=""
    for element in element_list:
        concatenated_string+=element

    return concatenated_string

def main():
    try:
        no_of_element=int(input("enter the no. of element you need to add: "))
        element_list=[]
        print("add element")
        for _ in range(no_of_element):
            element_list.append(input())

        print(f"after concatenating the list {element_list}: {concatenate_to_str(element_list)}") 
    except ValueError:
        print("invalid. Enter integer value") 

if __name__=="__main__":
    main()
