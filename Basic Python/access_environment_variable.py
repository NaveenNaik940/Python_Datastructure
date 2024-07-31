'''

@Author:Naveen Madev Naik
@Date: 2024-07-26 15:51:00
@Last Modified by: Naveen Madev Naik
@Last Modified time: 2024-07-26 15:51:00
@Title :program to access environment variables.

'''


import os

def list_all_environment_variables():


    """
    Description:
        Function will print the environment variable in key value pair
    Parameter:
        None
    Return:
        None        
    """
    try:
        for key, value in os.environ.items():
            print(f"{key}={value}")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    list_all_environment_variables()

if __name__ == "__main__":
    main()
