# Create a program to prompt the user for hours and rate per hour and then calculate and display their weekly, monthly, and annual gross pay (hours * rate). Base monthly and annual calculations on 12 months per year and 52 weeks per year.

print(" How many weekly hours did you work ?")
Hourly = float(input())
print(" What is your rate foy pay ?")
Rate = float(input())

weekly = Rate * Hourly
monthly = weekly * 4
yearly = weekly * 52

print("Salary in Weekly: " + str(weekly))
print("Salary in Monthly: " + str(monthly))
print("Salary in Yearly: " + str(yearly))
