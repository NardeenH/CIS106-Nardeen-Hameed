def maxim():
    print("Real age is not what we have reached, but rather how we feel inside. - Gabriel García Márquez")

def yourAge():
    print("What is your age?")
    age = int(input())
    if age > 18:
        print(age > 18)
        print(" Allow To Drive ")
    else:
        print(age < 18)
        print("Not Allow To Drive")

# Main
# Create a program that asks the user how old they are in years, and then calculate and display their approximate age in months, days, hours, and seconds. For example, a person 1-year-old is 12 months old, 365 days old.
print("Enter you age?")
age = int(input())
months = age * 12
days = age * 365
hours = 365 * 24 * age
seconds = 60 * 60 * 24 * 365 * age
print(" Person age in months =" + str(months))
print(" Person age in days = " + str(days))
print(" Person age in hours = " + str(hours))
print(" Person age in seconds = " + str(seconds))
yourAge()
maxim()
