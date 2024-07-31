'''

@Author:Naveen Madev Naik
@Date: 2024-07-26 12:20:00
@Last Modified by: Naveen Madev Naik
@Last Modified time: 2024-07-26 12:20:00
@Title :program to print out a set containing all the colors from color_list_1 which
        are not present in color_list_2.

'''


def color_set(color_list1,color_list2):

    
    """
    Description:
        Function will reurn the set containing color that is not presenting in color_list2
    Parameter:
        color_list1,color_list2: we used to compare this parameter for returning set containg color which is not presenting in color list 2
    return:
        set        
    """


    color_set=set() 
    for color in color_list1:
        if color not in color_list2:
            color_set.add(color)
           
    return color_set

def main():
    try:
        element_in_list1=int(input("Enter the number of color you want to input in list1: "))
        color_list1=[]
        for _ in range(element_in_list1):
            color_list1.append(input(": ").lower())

        element_in_list2=int(input("Enter the number of color you want to input in list2: "))
        color_list2=[]
        for _ in range(element_in_list2):
            color_list2.append(input(": ").lower())  
         
        print(f"color which is not in color list 2: {color_set(color_list1,color_list2)}")

    except ValueError:
        print("invalid input. Enter intger element: ") 

if __name__=="__main__":
    main()
