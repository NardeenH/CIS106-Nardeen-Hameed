# Create a program to prompt the user for hours and rate per hour and then calculate and display their weekly, monthly, and annual gross pay (hours * rate). Base monthly and annual calculations on 12 months per year and 52 weeks per year.
print(" How many weekly hours did you work ?")
hours = float(input())
print(" What is your rate foy pay ?")
rate = float(input())
weekly = rate * hours
monthly = weekly * 30*4
yearly = weekly * 365*12
print("Salary in Weekly: " + str(weekly))
print("Salary in Monthly: " + str(monthly))
print("Salary in Yearly: " + str(yearly))
