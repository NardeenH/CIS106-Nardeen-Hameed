def calPayment(hours, rate):
    pay = hours * rate
    displayReuglarHours(hours, rate, pay)

def displayReuglarHours(hours, rate, pay):
    print("The payment for Regula Hours is:" + str(pay))

def getHours():
    print("Enter Hours:")
    hours = float(input())
    
    return hours

def getRate():
    print("Enter Rate per Hour:")
    rate = float(input())
    
    return rate

def overTimePayment(hours, rate):
    pay = 40 * rate + (hours - 40) * 1.5 * rate
    overtimeResult(hours, rate, pay)

def overtimeResult(hours, rate, pay):
    print("The payment for Overtime Hours is" + str(pay))

# Main
# Create a program to prompt the user for hours and rate per hour to compute gross pay (hours * rate). Include a calculation to give 1.5 times the hourly rate for any overtime (hours worked above 40 hours).[3] For example, 50 hours worked at $10 per hour with overtime is $550.
hours = getHours()
rate = getRate()
if hours <= 40:
    calPayment(hours, rate)
else:
    if hours > 40:
        overTimePayment(hours, rate)
    else:
        print("Put the right Data")
