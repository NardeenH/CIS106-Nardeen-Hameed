# Distance Converter

miles = int(input("What is the distance in miles?"))

DISTANCE_IN_FEET = miles * 5280
DISTANCE_IN_YARD = miles * 1760
DISTANCE_IN_INCHES = miles * 63360

print("The distance in feet is = " + str(DISTANCE_IN_FEET))
print("The distance in yard is = " + str(DISTANCE_IN_YARD))
print("The distance in inches is = " + str(DISTANCE_IN_INCHES))

