# Review MathsIsFun: Area of Plane Shapes. Create a program that asks the user for the dimensions of different shapes and then calculate and display the area of the shapes. Do not include shape choices. That will come later. For now, just include multiple shape calculations in sequence.
print("What is the length of the room?")
length = int(input())
print(" what is the width of the room? ")
width = int(input())
print(" what is the hight of the room?")
height = int(input())
print("what is the price per gallon? ")
price = int(input())
print(" how many square feet a gallon need ? ")
gallon = int(input())
area = 2 * length * height + 2 * width * height
gallon = area / gallon + 0.999
price = gallon * price
print(" total paint need to cover the room : " + str(gallon))
print(" price of paint is : " + str(price))
