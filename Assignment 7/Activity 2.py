def getAge():
    print("How old you are in years?")
    userAge = int(input())
    
    return userAge

def getAnswer():
    print("If you Would like to know your age in months print M, in Day D  in hours H and in second S")
    userAnswer = input()
    
    return userAnswer

def processDay(userAge):
    day = userAge * 365
    print("Your age is days is " + str(day))
    
    return day

def processHour(userAge):
    hour = userAge * 24 * 365
    print(" You Age in hours is " + str(hour))
    
    return hour

def processMonth(userAge):
    month = userAge * 12
    print(" your age in months is" + str(month))
    
    return month

def processSecond(userAge):
    second = userAge * 365 * 24 * 60 * 60
    print("Your age in seconds is  " + str(second))
    
    return second

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
