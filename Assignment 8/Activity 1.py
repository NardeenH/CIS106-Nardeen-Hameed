def doLoop(value, exp):
    i = 1
    while True:    #This simulates a Do Loop
        print(str(value) + "*" + str(i) + " = " + str(value * i))
        i = i + 1
        if not(i <= exp): break   #Exit loop

def forLoop(value, exp):
    i = 1
    for i in range(1, 100 + 1, 1):
        print(str(value) + "*" + str(i) + " = " + str(value * i))

def getExp():
    print("Enter the Number of Expressions:")
    exp = int(input())
    
    return exp

def getValue():
    print("Enter Value:")
    value = int(input())
    
    return value

def whileLoop(value, exp):
    i = 1
    while i <= exp:
        print(str(value) + "*" + str(i) + " = " + str(value * i))
        i = i + 1

# Main
value = getValue()
exp = getExp()
whileLoop(value, exp)
doLoop(value, exp)
forLoop(value, exp)
