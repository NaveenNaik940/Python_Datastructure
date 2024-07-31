'''

@Author:Naveen Madev Naik
@Date: 2024-07-25 12:23:00
@Last Modified by: Naveen Madev Naik
@Last Modified time: 2024-07-25 12:23:00
@Title :program which accepts a sequence of comma-separated numbers from user
        and generate a list and a tuple with those numbers

'''


def string_to_list_tuple(number):


    """
    Description:
           function will return the list of number and tuple

    Parameter:
        stringNumber: it is input from user 

    return:
        list: listNumber  
        tuple: tupleNumber    
    """

    
    stringNumber=number.split(",")
    
    listNumber=[]
    for number in stringNumber:
        if number!= '':
            listNumber.append(number)
    
    tupleNumber=tuple(listNumber) 

    return listNumber,tupleNumber

def main():
    # Input from the user
    try:
        stringNumber= input("Enter Your first name:")
        for check in stringNumber:
            if check.isdigit() or check in ',':
                pass
            else:
                raise ValueError(f"invalid input {check}")
        listNumber,tupleNumber=string_to_list_tuple(stringNumber)
        print(f"{listNumber},{tupleNumber}")
        
    except ValueError as e:
        print(f"{e}")

if __name__=="__main__":
    main()    
        
        