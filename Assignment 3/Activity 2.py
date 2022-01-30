print(" How old are you ?")
age = float(input())
month = age * 12
days = age * 12 * 365
hours = (age * 12 * 365 + age / 4) * 24
second = (age * 12 * 365 + age / 4) * 24 * 60 * 60
print(" age in month= " + str(month))
print(" age in days= " + str(days))
print(" age in hours = " + str(hours))
print(" age in second = " + str(second))
