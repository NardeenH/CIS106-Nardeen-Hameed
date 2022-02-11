# Reading hours and rates from user.


def get_hourly():
    print("How many hours per week?")
    hourly = float(input())
    return hourly


def get_rate():
    print("what's the rate per week?")
    rate = float(input())
    return rate


def calculateWeekly(hourly, rate):
    weekly = rate * hourly
    return weekly


def  calculateMonthly(weekly):
    monthly = weekly * 4
    return monthly


def calculateYearly(weekly):
    yearly = weekly * 52
    return yearly


def displayRuselt(weekly, monthly, yearly):
    print("Salary in weekly is= " + str(weekly))
    print("Salary in monthly is =" + str(monthly))
    print("Salary in yearly is =" + str(yearly))
    
    
# Main
hourly = get_hourly()
rate = get_rate()
weekly = calculateWeekly(hourly, rate)
monthly = calculateMonthly(weekly)
yearly = calculateYearly(weekly)
displayRuselt(weekly, monthly, yearly)
