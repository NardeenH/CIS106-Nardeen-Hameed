def dayResult(day):
    print("Your Age in Days is:" + str(day))

def getAge():
    print("How old you are in years?")
    userAge = int(input())
    
    return userAge

def getAnswer():
    print("If you Would like to know your age print:M for months: D for days:H for hours: S for seconds:")
    userAnswer = input()
    
    return userAnswer

def hoursResult(hour):
    print("You Age in Hours is:" + str(hour))

def monthResult(month):
    print(" your age in months is:" + str(month))

def processDay(userAge):
    day = userAge * 365
    dayResult(day)
    
    return day

def processHour(userAge):
    hour = userAge * 24 * 365
    hoursResult(hour)
    
    return hour

def processMonth(userAge):
    month = userAge * 12
    monthResult(month)
    
    return month

def processSecond(userAge):
    second = userAge * 365 * 24 * 60 * 60
    secondResult(second)
    
    return second

def secondResult(second):
    print("Your Age in Seconds is:" + str(second))

# Main
# Create a program that asks the user how old they are in years. Then ask the user if they would like to know how old they are in (M)onths, (D)ays, (H)ours, or (S)econds. Use if/else conditional statements to display their approximate age in the selected timeframe. Do not perform any unnecessary calculations.
userAge = getAge()
userAnswer = getAnswer()
if userAnswer == "M":
    processMonth(userAge)
else:
    if userAnswer == "D":
        processDay(userAge)
    else:
        if userAnswer == "H":
            processHour(userAge)
        else:
            if userAnswer == "S":
                processSecond(userAge)
            else:
                print("Please enter correct data!")
