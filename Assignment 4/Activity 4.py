# Create a program that asks the user for a distance in miles, and then calculate and display the distance in yards, feet, and inches, or ask the user for a distance in miles, and then calculate and display the distance in kilometers, meters, and centimeters.
print(" What is the Distance ? ")
distance = int(input())
distanceFeet = distance * 12
distanceYard = distance * 3
distanceMile = distance * 5280
print(" The distance in Feet is = " + str(distanceFeet))
print(" The distance in Yard is = " + str(distanceYard))
print(" The distance in mile is = " + str(distanceMile))
