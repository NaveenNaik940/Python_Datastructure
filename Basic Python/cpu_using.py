'''

@Author:Naveen Madev Naik
@Date: 2024-07-26 15:20:00
@Last Modified by: Naveen Madev Naik
@Last Modified time: 2024-07-26 15:20:00
@Title :program to find out the number of CPUs using.

'''


import os

def get_cpu_count():

    """
    Description:
        print the number of cpus are pc is using 
    Parameter:
        None
    Return:
        None        
    """
    try:
        cpu_count = os.cpu_count()
        if cpu_count is None:
            print("Unable to determine the number of CPUs.")
        else:
            print(f"Number of CPUs: {cpu_count}")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    input("Press enter to check how many cpus are available ")
    get_cpu_count()

if __name__ == "__main__":
    main()
