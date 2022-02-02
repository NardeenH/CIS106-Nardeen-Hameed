# Create a program to prompt the user for hours and rate per hour and then calculate and display their weekly, monthly, and annual gross pay (hours * rate). Base monthly and annual calculations on 12 months per year and 52 weeks per year.
print(" How many weekly hours did you work ?")
hours = int(input())
print(" What is your rate foy pay ?")
rate = int(input())
salary = rate * hours
weekly = salary * 7
monthly = salary * 30 * 12
yearly = salary * 52 * 7
print("Salary in Weekly: " + str(weekly))
print("Salary in Monthly: " + str(monthly))
print("Salary in Yearly: " + str(yearly))
