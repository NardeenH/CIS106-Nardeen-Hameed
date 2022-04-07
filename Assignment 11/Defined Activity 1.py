# difined Activity


def get_year():
    print("Enter the year")
    year = int(input())
    return year


def get_month():
    print(" Enter the month in number")
    month = int(input())
    return month


def leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print("The year", year, " is a leap year")
        return True
    else:
        print("The year", year, "is not a leap year")
        return False
            
            
def display_result(month_name, month_days):
    print(month_name, "has", month_days, "days:")
    return month_name


def get_month_days(month, year):
    days = [0, 31, 28, 31, 30, 31, 30, 31, 30, 31, 30, 31]
    leap = leap_year(year)
    if leap:
        days[2] = 29
    else:
        days[2] = 28
    month_days = days[month]
    return month_days


def get_month_name(month):
    months = ['', 'January', 'February', 'March', 'April', 'May',
                  'June', 'July', 'August', 'September',
                  'October', 'November', 'December']
    month_name = months[month]
    return month_name

            
def main():
    while True:
        year = get_year()
        if year <= 0:
            break
        month = get_month()
        if month < 1 or month > 12:
            break   
        month_name = get_month_name(month)
        month_days = get_month_days(month, year)
        display_result(month_name, month_days)
    
    
main()
           