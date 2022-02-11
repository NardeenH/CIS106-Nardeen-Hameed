def calculateMonthly(weekly):
    monthly = weekly * 4
    
    return monthly

def calculateWeekly(hourly, rate):
    weekly = rate * hourly
    
    return weekly

def calculateYearly(weekly):
    yearly = weekly * 52
    
    return yearly

def displayRuselt(weekly, monthly, yearly):
    print("Salary in weekly is= " + str(weekly))
    print("Salary in monthly is =" + str(monthly))
    print("Salary in yearly is =" + str(yearly))

def getHourly():
    print("How many hours you works?")
    hourly = int(input())
    
    return hourly

def getRate():
    print("What's your rate")
    rate = int(input())
    
    return rate

# Main
hourly = getHourly()
rate = getRate()
weekly = calculateWeekly(hourly, rate)
monthly = calculateMonthly(weekly)
yearly = calculateYearly(weekly)
displayRuselt(weekly, monthly, yearly)
