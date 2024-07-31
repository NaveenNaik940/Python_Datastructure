'''

@Author:Naveen Madev Naik
@Date: 2024-07-25 14:14:00
@Last Modified by: Naveen Madev Naik
@Last Modified time: 2024-07-25 14:14:00
@Title :program to print the documents of Python built-in
        function.

'''


import builtins

def list_builtin_functions():
    """
    Description:
          Function will list all the callable function
    Parameter:
          None
    Return:
       None            
    """
    # Get all attributes of the builtins module
    builtin_names = dir(builtins)
    
    # Filter only functions
    builtin_functions = [name for name in builtin_names if callable(getattr(builtins, name))]
    
    print("List of built-in functions in Python:\n")
    count=1
    for func in sorted(builtin_functions):
        print(f"{count}:{func}()")
        count+1




def print_builtin_function_docs(func_name):


    """
    Description:
        Function will print the documentation of given function name
    parameter:
        func_name:it will take the input from the user to check its function description
    return:
        None         
    """

    
    try:
        # Get the built-in function object by name
        func = eval(func_name)
        if callable(func):
            print(f"Documentation for built-in function '{func_name}':\n")
            help(func)
        else:
            print(f"'{func_name}' is not a built-in function.")
    except NameError:
        print(f"'{func_name}' is not a valid built-in function name.")

def main():
    while True:
        func_name = input("Enter the name of a built-in function (or 'exit' to quit): ")
        if func_name.lower() == 'exit':
            break
        print_builtin_function_docs(func_name)

if __name__ == "__main__":
    list_builtin_functions()
    main()
