def getHours():
    print("Enter hours")
    hours = int(input())
    
    return hours

def getRate():
    print("Enter rate per hours")
    rate = float(input())
    
    return rate

# Main
# Create a program to prompt the user for hours and rate per hour to compute gross pay (hours * rate). Include a calculation to give 1.5 times the hourly rate for any overtime (hours worked above 40 hours).[3] For example, 50 hours worked at $10 per hour with overtime is $550.
hours = getHours()
rate = getRate()
if hours <= 40:
    pay = hours * rate
else:
    if hours > 40:
        pay = 40 * rate + (hours - 40) * 1.5 * rate
print(" GrossPay is " + str(pay))
