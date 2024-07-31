'''

@Author:Naveen Madev Naik
@Date: 2024-07-30 16:30:00
@Last Modified by: Naveen Madev Naik
@Last Modified time: 2024-07-30 16:30:00
@Title :script to generate and print a dictionary that contains a
        number (between 1 and n) in the form (x, x*x).

'''

def main():
    try:
        length_limit=int(input("enter the limit of length for dictionary "))
        square_dict={}
        for key in range(1,length_limit+1):
            square_dict[key]=key*key
        print(square_dict) 

    except ValueError as e:
        print(e)
    except Exception as e:
        print(e)           

if __name__=="__main__":
    main()