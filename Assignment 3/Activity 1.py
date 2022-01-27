# Create a program to prompt the user for hours and rate per hour and then calculate and display their weekly, monthly, and annual gross pay (hours * rate). Base monthly and annual calculations on 12 months per year and 52 weeks per year.[1]
# I got some help from Tim.
print(" How many hours did you work ")
hours = int(input())
print(" What is your rate foy pay ")
rate = int(input())
daily = hours * rate
weekly = daily * 7
monthly = daily * 30
annualy = weekly * 52
print("Salary in Weekly " + str(weekly))
print("Salary in Monthlu " + str(monthly))
print("Salary in Annualy " + str(annualy))
