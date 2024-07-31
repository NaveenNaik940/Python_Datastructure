'''

@Author:Naveen Madev Naik
@Date: 2024-07-26 15:20:00
@Last Modified by: Naveen Madev Naik
@Last Modified time: 2024-07-26 15:20:00
@Title :program to list all files in a directory in Python.

'''


import os

def list_file(directory_path):
    

    """
    Description:
        function will list all the file in the given directory
    Parameter:
        directory_path: user given directory      
    Return:
        list: files_in_directory     
    """


    # List files in the directory
    files_in_directory = os.listdir(directory_path)

    return files_in_directory

def main():
    try:
        directory_path=input("copy paste valid directory path: ")
        print(f"{list_file(directory_path)}")

    except Exception as e:
        print(e)  

if __name__=="__main__":
    main()