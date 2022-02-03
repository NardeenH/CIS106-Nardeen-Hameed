# Create a program to prompt the user for hours and rate per hour and then calculate and display their weekly, monthly, and annual gross pay (hours * rate). Base monthly and annual calculation on 12 months per year and 52 weeks per year.
#reading hours and rates from user

hours = float(input("Enter Weekly hours:"))
rate = float(input("Enter rate:"))
#finding weekly salary
weekly = rate * hours * 7
#Finding monthly salary
monthly = weekly * 30
#finding yearly salary
yearly = weekly * 52

print("weekly = ", weekly)
print("montly = " , monthly)
print ("yearly = ", yearly)