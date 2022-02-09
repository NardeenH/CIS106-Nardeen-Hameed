def calculateArea(length, width):
    area = length * width
    
    return area

def calculateareainYard(area):
    yard = area / 9.0
    
    return yard

def displayRuselt(area, yard):
    print("The area is=" + str(area))
    print("The area in yard is=" + str(yard))

def getLength():
    print("Enter the length")
    length = float(input())
    
    return length

def getWidth():
    print("Enter Width")
    width = float(input())
    
    return width

# Main
# Create a program that calculates the area of a room to determine the amount of floor covering required. The room is rectangular with the dimensions measured in feet with decimal fractions. The output needs to be in square yards. There are 3 linear feet (9 square feet) to a yard.
length = getLength()
width = getWidth()
area = calculateArea(length, width)
yard = calculateareainYard(area)
displayRuselt(area, yard)
