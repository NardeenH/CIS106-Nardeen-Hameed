# reading hours and rates from user 

WEEKS_PER_MONTH = 4
WEEKS_PER_YEAR = 52

hours = float(input("How many weekly hours do you work?"))
rate = float(input("What is the rate of pay?"))

weekly = rate * hours 
monthly = weekly * WEEKS_PER_MONTH
yearly = weekly * WEEKS_PER_YEAR

print("weekly = ", weekly)
print("monthly = ", monthly)
print("yearly = ", yearly)