'''

@Author:Naveen Madev Naik
@Date: 2024-07-26 12:20:00
@Last Modified by: Naveen Madev Naik
@Last Modified time: 2024-07-26 12:20:00
@Title :program to check whether a file exists.

'''


import os

def is_file_exist(directory_path,file_to_check):
    

    """
    Description:
        function will print the whether given file exist in given directory
    Parameter:
        directory_path: user given directory
        file_to_check: use this file to check whether this file is there in given directory   
    Return:
        None     
    """

    # List files in the directory
    files_in_directory = os.listdir(directory_path)
    

    # Check if the specific file exists
    if file_to_check in files_in_directory:
        print(f"{file_to_check} exists in the directory.")
    else:
        print(f"{file_to_check} does not exist in the directory.")
        print("Files in directory:", files_in_directory)

def main():
    try:
        directory_path=input("copy paste valid directory path: ")
        file_to_check=input("enter valid file to check: ")
        is_file_exist(directory_path,file_to_check)

    except Exception as e:
        print(e)  

if __name__=="__main__":
    main()