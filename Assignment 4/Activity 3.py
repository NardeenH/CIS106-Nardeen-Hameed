# Distance Converter

miles = int(input("What is the distance in miles?"))

DISTANCE_FEET = miles * 5280
DISTANCE_YARD = miles * 1760
DISTANCE_INCHES = miles * 63360

print("The distance in feet is = " + str(DISTANCE_FEET))
print("The distance in yard is = " + str(DISTANCE_YARD))
print("The distance in inches is = " + str(DISTANCE_INCHES))


