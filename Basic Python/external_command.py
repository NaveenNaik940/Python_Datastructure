'''

@Author:Naveen Madev Naik
@Date: 2024-07-26 12:20:00
@Last Modified by: Naveen Madev Naik
@Last Modified time: 2024-07-26 12:20:00
@Title :program to call an external command in Python.

'''


import os
import platform

def execute_command(command):


    """
    Description:
        Function will print the output of valid command entered
    Parameter:
        command: takes input form user  
    return:
        None      
    """
    
    
    system = platform.system()

    if system == 'Windows':
        shell = True  
    else:
        shell = False

    try:
        
        with os.popen(command) as stream:
            output = stream.read()
        if not output:
            print("No output from the command.")
        else:
            print("Command output:\n", output)
    
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    try:
        user_command = input("Enter the command to execute: ")
        if not user_command.strip():
            raise ValueError("Command cannot be empty.")
        execute_command(user_command)
    
    except ValueError as ve:
        print(f"Value error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
