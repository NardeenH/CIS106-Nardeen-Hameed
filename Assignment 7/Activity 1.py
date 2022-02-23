def calPayment(hours, rate):
    pay = hours * rate
    print("The Payment for Regular Hours is" + str(pay))

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
    print("The payment for Overtime Hours is" + str(pay))

# Main
hours = getHours()
rate = getRate()
if hours <= 40:
    calPayment(hours, rate)
else:
    if hours > 40:
        overTimePayment(hours, rate)
    else:
        print("Put the right Data")
