# difined Activity


def get_year():
    print("Enter the year")
    year = int(input())
    return year


def get_month():
    print(" Enter the month in number")
    month = input(str())
    return month


def leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False
            
            
def display_result(month_name, month_days, year):
    print(month_name + " " + str(year) + " has " + str(month_days) + " days.")
    

def get_month_days(month, year):
    days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    leap = leap_year(year)
    if leap:
        days[2] = 29
    else:
        days[2] = 28
    month_days = days[int(month)]
    return month_days


def get_month_name(month):
    months = ['', 'January', 'February', 'March', 'April', 'May',
                  'June', 'July', 'August', 'September',
                  'October', 'November', 'December']
    month_name = months[int(month)]
    return month_name

            
def main():
    while True:
        year = get_year()
        if year <= 0:
            break
        month = get_month()
        if int(month) < 1 or int(month) > 12:
            break   
        month_name = get_month_name(month)
        month_days = get_month_days(month, year)
        display_result(month_name, month_days, year)
    
    
main()
           