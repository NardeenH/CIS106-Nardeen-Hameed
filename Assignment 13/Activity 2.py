# Assainment 13, Actvity2
# Use string functions/methods to delete leading, trailing,
# and duplicate spaces, and then print the line of text backwards.
# https://www.datasciencemadesimple.com/remove-spaces-in-python/


def get_text():
    text = input("Enter Text:")
    return text


def remove_spaces(text):
    i = text
    i = text.lstrip()
    return i


def backwards_text(text):
    x = text
    x = (text[::-1])
    return x
    

def output_result(text):
    print(text.lstrip())
    print((text[::-1]))
    

def main():
    text = get_text()
    i = remove_spaces(text)
    x = backwards_text(text)
    output_result(text)
      
    
main()
