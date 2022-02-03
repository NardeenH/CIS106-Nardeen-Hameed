# Create a program to prompt the user for hours and rate per hour and then calculate and display their weekly, monthly, and annual gross pay (hours * rate). Base monthly and annual calculation on 12 months per year and 52 weeks per year.

print("Enter hourly")
hourly = float (input())
print("Enter rate")
rate = float (input())

weekly = rate * hourly
monthly = weekly * 4
yearly = weekly * 52

Output
print("weekly = ", weekly)
print(" montly = " , monthly)
print ( " yearly = ", yearly )