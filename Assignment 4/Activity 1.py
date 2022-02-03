# reading hours and rates from user 

hours = float(input("How many weekly hours do you work?"))
rate = float(input("What is the rate of pay?"))

weekly = rate * hours 
monthly = weekly * 4
yearly = weekly * 52

print("weekly = ", weekly)
print("monthly = ", monthly)
print("yearly = ", yearly)