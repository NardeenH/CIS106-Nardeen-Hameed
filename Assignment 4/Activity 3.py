# Distance Converter

YARDS_PER_MILE = 1760
FEET_PER_MILE = 5280
INCHES_PER_MILE = FEET_PER_MILE * 12

miles = int(input("What is the distance in miles?"))

feet = miles * FEET_PER_MILE
yards = miles * YARDS_PER_MILE
inches = miles * INCHES_PER_MILE

print("The distance in feet is = " + str(feet))
print("The distance in yard is = " + str(yards))
print("The distance in inches is = " + str(inches))
