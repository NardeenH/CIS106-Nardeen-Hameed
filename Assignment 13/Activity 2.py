# Assainment 13, Actvity2
# Use string functions/methods to delete leading, trailing,
# and duplicate spaces, and then print the line of text backwards.
# https://www.datasciencemadesimple.com/remove-spaces-in-python/


def get_text():
    print("Enter Text:")
    text = str(input())
    return text


def remove_spaces(text):
    text1 = text
    text1 = text.lstrip()
    return text1


def backwards_text(text):
    text2 = text
    text2 = (text[::-1])
    return text2
    

def output_result(text):
    print(text.lstrip())
    print((text[::-1]))
    

def main():
    text = get_text()
    text1 = remove_spaces(text)
    text2 = backwards_text(text)
    output_result(text)
      
    
main()
