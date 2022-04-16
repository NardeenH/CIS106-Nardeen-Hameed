# Assignment 13, Actvity3


def get_text():
    text = input('Enter last with comma: ')
    return text


def remove_comma(text):
    items = text.split(",")
    return items


def display_output(items):
    for i in items:
        print(i.strip())


def main():
    text = get_text()
    items = remove_comma(text)
    display_output(items)
    
     
main()
