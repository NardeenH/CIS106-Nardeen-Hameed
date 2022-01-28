# Create a program that calculates the area of a room to determine the amount of floor covering required. The room is rectangular with the dimensions measured in feet with decimal fractions. The output needs to be in square yards. There are 3 linear feet (9 square feet) to a yard.
print(" what is the lenght of rectangular in feet ")
l = int(input())
print(" What is the width of rectangular in feet ")
w = int(input())
area = l * w
yeard = float(area) / 9
print(str(yeard) + "  Square yeard")
