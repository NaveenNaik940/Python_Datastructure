'''

@Author:Naveen Madev Naik
@Date: 2024-07-29 12:28:00
@Last Modified by: Naveen Madev Naik
@Last Modified time: 2024-07-29 12:28:00
@Title :program to clone or copy a list.

'''


def clone_list(original_list):
    return list(original_list)

def main():
    try:
        no_of_element=int(input("enter the number element in the list: "))
        original_list=[]
        print("enter the element")
        for index in range(no_of_element):
            original_list.append(input(": "))
        cloned_list = clone_list(original_list)
        print(f"copy of  {original_list} : {cloned_list} ")

    except ValueError:
        print("invalid input")  
    except Exception as e:
        print(f"{e}")     

if __name__ == "__main__":
    main()
