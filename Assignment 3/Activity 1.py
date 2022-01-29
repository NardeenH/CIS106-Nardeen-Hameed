# Create a program to prompt the user for hours and rate per hour and then calculate and display their weekly, monthly, and annual gross pay (hours * rate). Base monthly and annual calculations on 12 months per year and 52 weeks per year.[1]
# I got some help from Tim.
print(" How many weekly hours did you work ?")
hours = int(input())
print(" What is your rate foy pay ?")
rate = int(input())
weekly = hours * rate
yearly = weekly * 52
monthly = float(yearly) / 12
print("Salary in Weekly: " + str(weekly))
print("Salary in Monthly: " + str(monthly))
print("Salary in Yearly: " + str(yearly))
