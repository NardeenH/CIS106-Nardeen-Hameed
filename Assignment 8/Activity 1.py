def callLoop():
    print("For Loop >>")

def displayForloop(value, exp, count):
    print(str(value) + " * " + str(count) + " = " + str(value * count))

def forLoop(value, exp):
    callLoop()
    count = getCount()
    for count in range(1, exp + 1, 1):
        displayForloop(value, exp, count)

def getCount():
    count = 1
    
    return count

def getExp():
    print("Enter the Number of Expressions:")
    exp = int(input())
    
    return exp

def getValue():
    print("Enter Value:")
    value = int(input())
    
    return value

# Main
# Create a program that uses a loop to generate a list of multiplication expressions for a given value. Ask the user to enter the value and the number of expressions to be displayed.
value = getValue()
exp = getExp()
forLoop(value, exp)
