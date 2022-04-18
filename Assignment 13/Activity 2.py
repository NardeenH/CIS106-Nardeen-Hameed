# Assainment 13, Actvity2
# Use string functions/methods to delete leading, trailing,
# and duplicate spaces, and then print the line of text backwards.
# https://www.datasciencemadesimple.com/remove-spaces-in-python/
# https://www.youtube.com/watch?v=DYc0AKF0Qmc&t=693s


def get_text():
    text = input("Enter line of Text\n")
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
    txt = (text[::-1])
    return txt
    
    
def remove_space(text):
    txt = ' '.join(text.split())
    return txt


def output_result(text):
    print(text)
    

def main():
    text = get_text()
#     i = remove_spaces(text)
#     s = text.strip(text)
#     d = get_split(text)
    txt = remove_space(text)
    txt = backwards_text(txt)
    output_result(txt)

        
main()
