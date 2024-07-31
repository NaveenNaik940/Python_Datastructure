'''

@Author:Naveen Madev Naik
@Date: 2024-07-26 10:13:00
@Last Modified by: Naveen Madev Naik
@Last Modified time: 2024-07-26 10:13:00
@Title :program to create a histogram from a given list of integers

'''


def plot_histogram(hist_list):


    """
    Description:
        Function will print histogram plot
    Parameter:
        hist_list: takes user input in list
    return:
       None         
    """


    hist_dict={}
    for key in hist_list:
        if key in hist_dict:
            hist_dict[key] += "*"
        else:
            hist_dict[key] = "*"
    print(f"Histogrm Plot of given list: {hist_list}")        
    for key in hist_dict:
        print(f"{key}: {hist_dict[key]}")           
    

def main():
    try:
        no_of_integer=int(input("Enter the number of integer you want to enter: "))
        hist_list=[]
        print("add values one by one: ")
        
        for _ in range(no_of_integer):
            hist_list.append(int(input("")))
        plot_histogram(hist_list)    

    except ValueError as e:
        print(e)        

if __name__=="__main__":
    main()