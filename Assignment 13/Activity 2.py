# Assainment 13, Actvity2
# Use string functions/methods to delete leading, trailing,
# and duplicate spaces, and then print the line of text backwards.
# https://www.datasciencemadesimple.com/remove-spaces-in-python/


def get_text():
    text = input("Enter Text:")
    return text


def remove_spaces(text):
    removespace = text
    removespace = text.lstrip()
    return 


def backwards_text(text):
    backwords = text
    backwords = (text[::-1])
    return backwords
    

def output_result(text):
    print(text.lstrip())
    print((text[::-1]))
    

def main():
    text = get_text()
    removespace = remove_spaces(text)
    backwords = backwards_text(text)
    output_result(text)
      
    
main()
