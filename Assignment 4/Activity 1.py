# Create a program to prompt the user for hours and rate per hour and then calculate and display their weekly, monthly, and annual gross pay (hours * rate). Base monthly and annual calculation on 12 months per year and 52 weeks per year.

hours = float(input("How many weekly hours do you work?"))
rate = float(input("What is the rate of pay?:"))

weekly = rate * hours 
monthly = weekly * 4
yearly = weekly * 52

print("weekly = ", weekly)
print("monthly = ", monthly)
print("yearly = ", yearly)