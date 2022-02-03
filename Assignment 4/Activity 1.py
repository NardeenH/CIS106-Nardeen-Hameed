# Create a program to prompt the user for hours and rate per hour and then calculate and display their weekly, monthly, and annual gross pay (hours * rate). Base monthly and annual calculation on 12 months per year and 52 weeks per year.

# reading hours and rates from user

hours = float(input("How many weekly hours do you work?"))
rate = float(input("What is the rate of pay?:"))

# finding weekly salary
weekly = rate * hours 
#Finding monthly salary
monthly = weekly * 4
# finding yearly salary
yearly = weekly * 52

print("weekly = ", weekly)
print("monthly = ", monthly)
print("yearly = ", yearly)