def cleaningUp():
    print(" Prof. Dave, Whenever I learned something, I smile, When I smiled, I remember you.")
    print("I like using flowchart:)")

# Main
# Create a program to prompt the user for hours and rate per hour and then calculate and display their weekly, monthly, and annual gross pay (hours * rate). Base monthly and annual calculations on 12 months per year and 52 weeks per year.
print(" How many weekly hours did you work ?")
hourly = float(input())
print(" What is your rate foy pay ?")
rate = float(input())
weekly = rate * hourly
monthly = weekly * 4
yearly = weekly * 52
print("Salary in Weekly: " + str(weekly))
print("Salary in Monthly: " + str(monthly))
print("Salary in Yearly: " + str(yearly))
cleaningUp()
