# Create a program that helps the user determine how much paint is required to paint a room and how much it will cost. Ask the user for the length, width, and height of a room, the price of a gallon of paint, and the number of square feet that a gallon of paint will cover. Calculate the total area of the four walls as 2 * length * height + 2 * width * height Calculate the number of gallons as: total area / square feet per gallon Note: You must round up to the next full gallon. To round up, add 0.9999 and then convert the resulting value to an integer. Calculate the total cost of the paint as: gallons * price per gallon
print("What is the length of the room?")
length = float(input())
print(" what is the width of the room? ")
width = float(input())
print(" what is the hight of the room?")
height = float(input())
print("what is the cost per gallon? ")
cost = float(input())
print(" how many square feet a gallon need for room? ")
sqfeet = int(input())
area = 2 * length * height + 2 * width * height
gallon = area / sqfeet + 0.9999
cost = gallon * cost
print(" total paint need to cover the room : " + str(gallon))
print(" price of paint is : " + str(cost))
