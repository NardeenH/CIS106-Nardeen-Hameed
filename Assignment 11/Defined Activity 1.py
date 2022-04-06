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
#     while year > 0 and  month < 13 and month > 0:
        print(month_name, "has", month_days, "days:")
#         month = int(input("\nEnter a month: "))
#     return month

def get_month_days(month, year):
    days = [0, 31, 28, 31, 30, 31, 30, 31, 30, 31, 30, 31]
    leap = leap_year(year)
#         print(months[month], "has", days[month], "days:")
    if leap == True:
        days[2] = 29
#         print(months[month], "has", days[month], "days:")
    else:
        days[2] = 28
    month_days = days[month]
    return month_days
#         print(months[month], "has", days[month], "days:")

def get_month_name(month):
     months = ['', 'January', 'February', 'March', 'April', 'May',
              'June', 'July', 'August', 'September',
              'October', 'November', 'December']
     month_name = months[month]
     return month_name

            
def main():
    year = get_year()
    month = get_month()
    month_name = get_month_name(month)
    month_days = get_month_days(month, year)
    display_result(month_name, month_days)
    
    
main()
           