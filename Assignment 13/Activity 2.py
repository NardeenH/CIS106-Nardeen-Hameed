# Assainment 13, Actvity2
# Use string functions/methods to delete leading, trailing,
# and duplicate spaces, and then print the line of text backwards.
# https://www.datasciencemadesimple.com/remove-spaces-in-python/


def get_text():
    text = input("Enter Text:\n")
    return text


def remove_spaces(text):
    delete_space = text
    delete_space = text.lstrip()
    return delete_space


def backwards_text(text):
    reverse_words = text
    reverse_words = (text[::-1])
    return reverse_words
    

def output_result(text):
#     print(text.lstrip())
    print((text[::-1]))
    

def main():
    text = get_text()
    delete_space = remove_spaces(text)
    reverse_words = backwards_text(text)
    output_result(text)
      
    
main()
