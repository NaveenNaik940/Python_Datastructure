'''

@Author:Naveen Madev Naik
@Date: 2024-07-29 12:00:00
@Last Modified by: Naveen Madev Naik
@Last Modified time: 2024-07-29 12:00:00
@Title :program to remove duplicates from a list.

'''


def remove_duplicate(sample_list):


    """
    Description:
        Function will remove the duplicate from the list

    Parameter:
        sample_list:list which contains duplicate element 

    Return:
        list            
    """
    

    duplicate_free_list=list(set(sample_list))
    return duplicate_free_list

def main():
    
    try:
        no_of_element=int(input("enter the number element in the list: "))
        duplicate_list=[]
        print("enter the element")
        for index in range(no_of_element):
            duplicate_list.append(input(": "))

        print(f"Duplicate free list of {duplicate_list}: {remove_duplicate(duplicate_list)}")

    except ValueError:
        print("invalid input")  
    except Exception as e:
        print(f"{e}")      

if __name__ == "__main__":
    main()
