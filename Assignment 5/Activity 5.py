def cleanUp():
    print("Enjoy using Flowchart")

# Main
# Create a program that calculates the area of a room to determine the amount of floor covering required. The room is rectangular with the dimensions measured in feet with decimal fractions. The output needs to be in square yards. There are 3 linear feet (9 square feet) to a yard.
print(" what is the length of rectangular in feet ?")
length = float(input())
print(" What is the width of rectangular in feet ?")
width = float(input())
area = length * width
print(" area = " + str(area) + " feet ")
yard = area / 9
print(" area = " + str(yard) + " square yard ")
cleanUp()
