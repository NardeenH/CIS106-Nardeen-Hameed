# Assainment 13, Actvity2
# Use string functions/methods to delete leading, trailing,
# and duplicate spaces, and then print the line of text backwards.
# https://www.datasciencemadesimple.com/remove-spaces-in-python/


def get_text():
    text = input("Enter Text\n")
    return text

# def text_strip(text):
#     s = text.strip()
#     return s

# 
# def get_split(text):
#     d = ' '.join(text.split())
#     return d

#     i = text
#     if '  ' in text:
#         while '  ' in text:
#             text = text.replace('  ', ' ')
#     return i


def backwards_text(text):
#     x = ' '.join(text.split())
    x = (text[::-1])
    return x
    
    
def remove_space(text):
    x = ' '.join(text.split())
    return x


def output_result(text):
    print(text)
    

def main():
    text = get_text()
#     i = remove_spaces(text)
#     s = text.strip(text)
#     d = get_split(text)
    x = remove_space(text)
    x = backwards_text(x)
    output_result(x)

      
    
main()
