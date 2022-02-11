# Reading hours and rates from user.


def get_hourly():
    print("How many hours per week?")
    hourly = float(input())
    return hourly


def get_rate():
    print("what's the rate per week?")
    rate = float(input())
    return rate


def calculate_weekly(hourly, rate):
    weekly = rate * hourly
    return weekly


def calculate_monthly(weekly):
    monthly = weekly * 4
    return monthly


def calculate_yearly(weekly):
    yearly = weekly * 52
    return yearly


def display_ruselt(weekly, monthly, yearly):
    print("Salary in weekly is= " + str(weekly))
    print("Salary in monthly is =" + str(monthly))
    print("Salary in yearly is =" + str(yearly))
    
    
def main():
    hourly = get_hourly()
    rate = get_rate()
    weekly = calculate_weekly(hourly, rate)
    monthly = calculate_monthly(weekly)
    yearly = calculate_yearly(weekly)
    display_ruselt(weekly, monthly, yearly)
    
    
main()    