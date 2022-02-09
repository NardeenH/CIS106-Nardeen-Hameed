def calculateDays(age):
    days = age * 365
    
    return days

def calculateHours(age):
    hours = age * 24 * 365
    
    return hours

def calculateMonths(age):
    months = age * 12
    
    return months

def calculateSeconds(age):
    seconds = age * 365 * 24 * 60 * 60
    
    return seconds

def displayResult(months, days, hours, seconds):
    print("Age in months is =" + str(months))
    print("Age in days is=" + str(days))
    print(" Age in hours is=" + str(hours))
    print("Age in seconds is=" + str(seconds))

def getAge():
    print("Enter your age?")
    age = int(input())
    
    return age

# Main
# Create a program that asks the user how old they are in years, and then calculate and display their approximate age in months, days, hours, and seconds. For example, a person 1-year-old is 12 months old, 365 days old.
age = getAge()
months = calculateMonths(age)
days = calculateDays(age)
hours = calculateHours(age)
seconds = calculateSeconds(age)
displayResult(months, days, hours, seconds)
