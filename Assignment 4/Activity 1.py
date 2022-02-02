# It's first time i will type in IDE. Let try to Create programe.
#Create a program to prompt the user for hours and rate per hour and then calculate and display their weekly, monthly, and annual gross pay (hours * rate). Base monthly and annual calculations on 12 months per year and 52 weeks per year.
print(" How many weekly hours you work ")
Hours = float(input())
print (" what is your rare for pay " )
Rate = float( input())
salary = Rate * Hours
weekly = salary * 7
monthly = salary *30 * 12
yearly = salary * 52 * 7
print ( " salary in weekly: " + str(weekly))
print ( " salary in monthly: " + str(monthly))
print ( " salary in yearly: " + str(yearly))

