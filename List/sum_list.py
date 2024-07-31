'''

@Author:Naveen Madev Naik
@Date: 2024-07-29 11:00:00
@Last Modified by: Naveen Madev Naik
@Last Modified time: 2024-07-29 11:00:00
@Title :program to sum all the items in a list.

'''


def sum_list(given_list):
    

    """
    Description:
        Function will return the sum of all the element in the list
    Parameter:
        given_list:used to sum the all the element present in the list
    Return:
        int   
    """
    return sum([element for element in given_list])

def main():
    try:
        no_of_element = int(input("Enter the number element in the list: "))
        example_list=[]
        print("enter the element i the list one by one")
        for element in range(no_of_element):
            example_list.append(int(input(": ")))
        print(f"the sum all the element in the list {example_list} is : {sum_list(example_list)}")    

    except ValueError as e:
        print(f"{e}")    

if __name__ == "__main__":
    main()
