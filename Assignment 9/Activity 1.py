def getCount():
    count = 1
    
    return count

def getExpressions():
    print("Enter Number of Expressions")
    expressions = int(input())
    
    return expressions

def getValue():
    print(" Enter Value:")
    value = int(input())
    
    return value

def processExpression(value, expressions):
    count = getCount()
    while count <= expressions:
        print(str(value) + "*" + str(count) + "=" + str(value * count))
        count = count + 1

# Main
# Create a program that uses a loop to generate a list of multiplication expressions for a given value. Ask the user to enter the value and the number of expressions to be displayed.
value = getValue()
expressions = getExpressions()
processExpression(value, expressions)
