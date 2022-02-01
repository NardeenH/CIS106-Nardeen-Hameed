# Create a program that asks the user how old they are in years, and then calculate and display their approximate age in months, days, hours, and seconds. For example, a person 1-year-old is 12 months old, 365 days old.
print(" How old are you ? ")
age = int(input())
months = age * 12
days = age * 12 * 365 + float(age) / 4
hours = (age * 12 * 365 + float(age) / 4) * 24
minutes = (age * 365 + float(age) / 4) * 24 * 60
seconds = (age * 365 + float(age) / 4) * 24 * 60 * 60
print(" Person age in months" + str(months))
print(" Person age in days = " + str(days))
print(" Person age in hours = " + str(hours))
print(" Person age in minutes = " + str(minutes))
print(" Person age in seconds = " + str(seconds))
