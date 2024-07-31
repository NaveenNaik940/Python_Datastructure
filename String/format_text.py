'''

@Author:Naveen Madev Naik
@Date: 2024-07-27 11:30:00
@Last Modified by: Naveen Madev Naik
@Last Modified time: 2024-07-27 11:30:00
@Title :program to display formatted text (width=50) as output

'''


def format_text(text, width):


    """
    Description:
        function to format text enter to specific width
    Parameter:
        text:user input will convert into specific width by formating
        width: user specified width
    Return: 
        string       
    """

    
    words = text.split()
    formatted_text = ""
    line = ""
    
    for word in words:
        # Check if adding the next word exceeds the width
        if len(line) + len(word) + 1 > width:
            # If it does, add the current line to formatted text and reset the line
            formatted_text += line.rstrip() + "\n"
            line = word + " "
        else:
            # If it doesn't, add the word to the current line
            line += word + " "
    
    # Add any remaining text in the line
    formatted_text += line.rstrip() + "\n"
    return formatted_text

def main():
    try:
        sample_text=input("enter the sample text you want to convert to specific width: ")
        width = int(input("enter the width you want to specify"))  
        formatted_text = format_text(sample_text, width)
        print(formatted_text)

    except ValueError as e:
        print(f"{e}")    

if __name__ == "__main__":
    main()
