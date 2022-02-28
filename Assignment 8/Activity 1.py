def displayForloop(value, expression, count):
    print(str(value) + " * " + str(count) + " = " + str(value * count))

def forLoop(value, expression):
    count = 0
    for count in range(1, expression + 1, 1):
        displayForloop(value, expression, count)

def getCount(count):
    count = 1
    
    return count

def getExpression():
    print("Enter the Number of Expressions:")
    expression = int(input())
    
    return expression

def getValue():
    print("Enter Value:")
    value = int(input())
    
    return value

# Main
# Create a program that uses a loop to generate a list of multiplication expressions for a given value. Ask the user to enter the value and the number of expressions to be displayed.
value = getValue()
expression = getExpression()
forLoop(value, expression)
