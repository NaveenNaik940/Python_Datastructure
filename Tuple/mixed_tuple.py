'''

@Author:Naveen Madev Naik
@Date: 2024-07-30 10:30:00
@Last Modified by: Naveen Madev Naik
@Last Modified time: 2024-07-30 10:30:00
@Title :program to create a tuple with different data types.


'''


def main():
    try:
        user_input = input("Enter values separated by spaces: ")
        
        elements = user_input.split()
        
        mixed_elements = []
        for element in elements:
            if element.isdigit():
                mixed_elements.append(int(element))
            elif element.replace('.', '', 1).isdigit() and element.count('.') < 2:
                mixed_elements.append(float(element))
            elif element.lower() == 'true':
                mixed_elements.append(True)
            elif element.lower() == 'false':
                mixed_elements.append(False)
            else:
                mixed_elements.append(element)
        
        created_tuple = tuple(mixed_elements)
        print(f"the mixed tuple is: {created_tuple}")

    except Exception as e:
        print(e)

if __name__=="__main__":
    main()    