# difined Activity


def get_year():
    print("Enter the year")
    year = int(input())
    return year


def get_month():
    print(" Enter the month number")
    month = int(input())
    return month


def leap_year(year):
    if (year % 4 == 0 and year%100 !=0) or ( year % 400 ==0):
        print("The year" year " is a leap year")
        return true
    else: 
        print("the year" year "is not a leap year")
        return false
            
            
def month_days(months, month):
    days = [0, 31, 28, 31, 30,31, 30, 31, 30, 31, 30, 31]
    month = ['','January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'Novemver', 'December']
    while month < 13 and month >0:
      print[month], "has", days[month],"days")
      print("\nEnter a month:"))
      month = int(input()
      return month
        

def main():
    year = get_year()
    month = get_ month()
    leap_year(year)
    month_days(months, month)
    
main()
           