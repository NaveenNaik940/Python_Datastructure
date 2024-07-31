'''

@Author:Naveen Madev Naik
@Date: 2024-07-29 12:00:00
@Last Modified by: Naveen Madev Naik
@Last Modified time: 2024-07-29 12:00:00
@Title :program to get a list, sorted in increasing order by the last
        element in each tuple from a given list of non-empty tuples.

'''


def sort_tuples_by_last_element(tuples_list):


    """
    Description:
        Function will return tuple list which is sorted from last index

    Parameter:
        tuples_list:we need to sort this tuple list 

    Return:
        list            
    """
    tuple_length = len(tuples_list)
    for outer_index in range(tuple_length):
        for inner_index in range(0, tuple_length-outer_index-1):
            if tuples_list[inner_index][-1] > tuples_list[inner_index+1][-1]:
                tuples_list[inner_index], tuples_list[inner_index+1] = tuples_list[inner_index+1], tuples_list[inner_index]
    return tuples_list

def main():
    
    try:
        tuple_list = []
        print("Enter tuples in the format (a,b) or type 'done' to finish:")

        while True:
            user_input = input("Enter a tuple: ")
            if user_input.lower() == 'done':
                break
            input_tuple = eval(user_input)
            if isinstance(input_tuple, tuple):
                tuple_list.append(input_tuple)
            else:
                print("Invalid input. Please enter a tuple.")  
        
        sorted_list = sort_tuples_by_last_element(tuple_list)
        
        print(f"Sorted list by the last element in each tuple: {sorted_list}")

    except ValueError:
        print("invalid input")  
    except Exception as e:
        print(f"{e}")      

if __name__ == "__main__":
    main()
