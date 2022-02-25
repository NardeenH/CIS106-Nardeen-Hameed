def doLoop(value, exp):
    count = 1
    print("Do Loop Counting:")
    while True:    #This simulates a Do Loop
        print(str(value) + "*" + str(count) + " = " + str(value * count))
        count = count + 1
        if not(count <= exp): break   #Exit loop

def forLoop(value, exp):
    count = 1
    print("For Loop Counting")
    for count in range(1, exp + 1, 1):
        print(str(value) + "*" + str(count) + " = " + str(value * count))

def getExp():
    print("Enter the Number of Expressions:")
    exp = int(input())
    
    return exp

def getValue():
    print("Enter Value:")
    value = int(input())
    
    return value

def whileLoop(value, exp):
    count = 1
    print("While Loop Counting:")
    while count <= exp:
        count = count + 1

# Main
# Create a program that uses a loop to generate a list of multiplication expressions for a given value. Ask the user to enter the value and the number of expressions to be displayed.
value = getValue()
exp = getExp()
forLoop(value, exp)
