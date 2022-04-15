# Assainment 13, Actvity 3
# # Create a program that asks the user for a line of text. Use string functions/methods to delete leading, trailing, and duplicate spaces, and then print the line of text backwards. For example:
#       the   cat   in   the   hat  
#     tah eht ni tac eht
# Use separate subroutines/functions/methods to implement input, each type of processing, and output. Avoid global variables by passing parameters and returning results.

def get_text():
    print("Enter your text:\n")
    text = str(input())
    return text

def deulicate(text):
    print(text[::-1])
    

def main():
    text = get_text()
    print(text[::-1])
    
    
main()