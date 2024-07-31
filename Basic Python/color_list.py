'''

@Author:Naveen Madev Naik
@Date: 2024-07-25 13:16:00
@Last Modified by: Naveen Madev Naik
@Last Modified time: 2024-07-25 13:16:00
@Title :program to display the first and last colors from the given list

'''


def first_last_color(color_list):
    """
    Description:
           function will return the first and last color from given list

    Parameter:
        color_list: list of color  

    return:
        firstColor: first  
        tuple: tupleNumber    
    """
    firstColor=color_list[0]
    lastColor=color_list[len(color_list)-1]

    return firstColor,lastColor

def main():
    # Input from the user
    try:
        color_num=int(input("enter how many color names you want to add:"))
        color_list=[]
        for color in range(color_num):
            color_list.append(input("add color: "))

        firstColor,lastColor =first_last_color(color_list) 
        print(f"first color in a list: {firstColor}\n",f"last color in the list: {lastColor}")  

    except ValueError:
        print(f"enter valid integer number")

if __name__=="__main__":
    main()    
        
        