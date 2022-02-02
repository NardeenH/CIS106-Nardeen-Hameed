# Create a program that asks the user for a distance in miles, and then calculate and display the distance in yards, feet, and inches, or ask the user for a distance in miles, and then calculate and display the distance in kilometers, meters, and centimeters.
print(" What is the Distance ? ")
distance = int(input())
distanceFeet = distance * 5280
distanceYard = distance * 1760
distanceInch = distance * 63360
distanceKilometer = distance * 1.6069344
distanceMeter = distance * 1609.34
distanceCentimeter = distance * 160934
print(" The distance in Feet is = " + str(distanceFeet))
print(" The distance in Yard is = " + str(distanceYard))
print(" The distance in Inch is = " + str(distanceInch))
print(" The distance in kilometer is = " + str(distanceKilometer))
print(" The distance in Meter is = " + str(distanceMeter))
print(" The distance in centimeter is = " + str(distanceCentimeter))
