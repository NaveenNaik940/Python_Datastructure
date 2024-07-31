'''

@Author:Naveen Madev Naik
@Date: 2024-07-29 11:40:00
@Last Modified by: Naveen Madev Naik
@Last Modified time: 2024-07-29 11:40:00
@Title :program to count the number of strings where the string length
        is 2 or more and the first and last character are same from a given list of strings.

'''


def count_string(given_list):
    

    """
    Description:
        Function will return count number of strings where the string length
        is 2 or more and the first and last character are same from a given list of strings 

    Parameter:
        given_list:given list

    Return:
        int   
    """


    count_string=0
    for string_element in given_list:
        if len(string_element)>=2 and string_element[0]==string_element[len(string_element)-1]:
            count_string+=1
    return count_string

def main():
    try:
        no_of_element = int(input("Enter the number element in the list: "))
        example_list=[]
        print("enter the string in the list one by one")
        for element in range(no_of_element):
            example_list.append((input(": ")))
        print(f"number of string in {example_list} which has length greater than or equal to 2  and first and last character are same
              : {count_string(example_list)}")    

    except ValueError as e:
        print(f"{e}")    

if __name__ == "__main__":
    main()
