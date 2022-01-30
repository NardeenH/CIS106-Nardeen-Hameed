# Create a program that asks the user how old they are in years, and then calculate and display their approximate age in months, days, hours, and seconds. For example, a person 1-year-old is 12 months old, 365 days old, etc.
# 
# I enjoy using flowchart.
print(" How old are you ?")
age = float(input())
month = age * 12
days = age * 12 * 365
hours = (age * 12 * 365 + age / 4) * 24
seconds = (age * 12 * 365 + age / 4) * 24 * 60 * 60
print(" age in month= " + str(month))
print(" age in days= " + str(days))
print(" age in hours = " + str(hours))
print(" age in seconds = " + str(seconds))
