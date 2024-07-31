'''

@Author:Naveen Madev Naik
@Date: 2024-07-29 11:19:00
@Last Modified by: Naveen Madev Naik
@Last Modified time: 2024-07-29 11:19:00
@Title :program to get the smallest number from a list.

'''


def smallest_number(given_list):
    

    """
    Description:
        Function will return smallest element in the list.

    Parameter:
        given_list:given list

    Return:
        int   
    """


    return sorted(given_list)[0]

def main():
    try:
        no_of_element = int(input("Enter the number element in the list: "))
        example_list=[]
        print("enter the element i the list one by one")
        for element in range(no_of_element):
            example_list.append(int(input(": ")))
        print(f"smallest element in the list {example_list} is : {smallest_number(example_list)}")    

    except ValueError as e:
        print(f"{e}")    

if __name__ == "__main__":
    main()
