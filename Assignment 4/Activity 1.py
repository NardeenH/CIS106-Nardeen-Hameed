# Create a program to prompt the user for hours and rate per hour and then calculate and display their weekly, monthly, and annual gross pay (hours * rate). Base monthly and annual calculations on 12 months per year and 52 weeks per year.
print(" How many weekly hours did you work?")
Hourly = float(input())
print (" What is your rate for pay?")
Rate = float(input())
Weekly= Rate* Hourly
Monthly = Weekly * 4
Yearly = Weekly * 52
print(" Salary in weekly: " + str(Weekly))
print(" Salary in Monthly: " + str(Monthly))
print(" Salary in Yearly: " + str(Yearly))
