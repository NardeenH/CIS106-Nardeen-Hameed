# Create a program that calculates the area of a room to determine the amount of floor covering required. The room is rectangular with the dimensions measured in feet with decimal fractions. The output needs to be in square yards. There are 3 linear feet (9 square feet) to a yard.
print(" what is the lenght of rectangular in feet ?")
lenght = float(input())
print(" What is the width of rectangular in feet ?")
width = float(input())
area = lenght * width
yard = area / 9
print(str(yard) + "  Square yard")
