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
            
            
def month_days(year, month):
    days = [0, 31, 28, 31, 30, 31, 30, 31, 30, 31, 30, 31]
    months = ['', 'January', 'February', 'March', 'April', 'May',
              'June', 'July', 'August', 'September', 'october', 'November', 'December']
    while month < 13 and month > 0:
      print(months[month], "has", days[month], "days:") 
      month = int(input())
      return month
        

def main():
    year = get_year()
    month = get_month()
    leap_year(year)
    month_days(year, month)
    
    
main()
           