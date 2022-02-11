# Distance Converter


def get_mile():
    print("Enter distance per mile")
    miles = int(input())
    return miles


def calculate_mile_in_yard(miles):
    yard = miles *1760
    return yard


def calculate_mile_in_feet(miles):
    feet = miles*5280
    return feet
    
    
def calculate_mile_in_inches(miles):
    inches = miles*63360
    return inches


def desplay_result(yard, feet, inches):
    print("The mile in yard is =" + str(yard))
    print("The mile in feet is =" + str(feet))
    print("The mile in inches is =" + str(inches))
    
    
def main():
    miles = get_mile()
    yard = calculate_mile_in_yard(miles)
    feet = calculate_mile_in_feet(miles)
    inches = calculate_mile_in_inches(miles)
    desplay_result(yard, feet, inches)
    

main()
