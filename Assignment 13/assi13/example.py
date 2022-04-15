import re

#method to get input
def getInput():
    txt = input("Enter a line of text: ")
    return txt

#method to remove the duplicate space
def removeDuplicate(txt):
    txt2 = txt.strip()
    txt3 = re.sub(' +', ' ',txt2)
    txt4 = txt3 [::-1]
    return txt4

#method to print the txt
def printText(txt):
    print(txt)

orignalText = getInput()
print("\nThe original text is: ")
printText(orignalText)

print("\nThe text after removing the duplicate blank space is: ")
UpdatedText = removeDuplicate(orignalText)
printText(UpdatedText)

