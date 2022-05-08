# https://www.youtube.com/watch?v=rFxXDO8-keg
# Final Project:
# Some help from Tim.
# https://thepythonguru.com/python-string-formatting/
# import urllib.request


import xml.etree.ElementTree as ET
import os


def read_url(filename):   
    xml = ET.parse(filename)
    return xml


def process_item(xml): 
    items = []
    for item in xml.iter('CD'):
        items.append({
            "title": item.find('TITLE').text,
            "artist": item.find('ARTIST').text,
            "country": item.find('COUNTRY').text,
            "price": item.find('PRICE').text,
            "year": item.find('YEAR').text}) 
    return items


def calcalate_average(items):
    total = 0
    count = 0
    os.system("")
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    print("%-30s %-s %-30s %-s %-30s %-s %-30s %-s %-30s" %
          (GREEN + "Title", " - ", RED + 'Artist',
           " - ", YELLOW + 'Country',
           " - ", BLUE + 'Price', " - ", MAGENTA + 'Year'))
    for element in items:
        print("%-30s %-s %-30s %-s %-30s %-s %-30s %-s %-30s" %(
            GREEN + element['title'],  " - ",
              RED + element['artist'], " - ",
              YELLOW + element['country'], " - ", 
              BLUE + element['price'], " - ",
              MAGENTA + element['year']))
        total = total + float(element['price'])
        count = count + 1
    return (count, total / count)
     
    
def main():
    CYAN = '\033[36m'
    RED = '\033[31m'
    YELLOW = '\033[33m'
    bold = '\033[1m'
    filename = "cd_catalog.xml"
    if os.path.isfile(filename):
        try:
            xml = read_url(filename)
            items = process_item(xml)
            count, average = calcalate_average(items)
            print((bold + " %d items, $%.2f average price.") % (count, average))
            print("__________________________________________________________________________________________________________________________")
            print(RED + "                              Professor DDDDave,YOU ARE THE BEST IN THE WEST!")
            print(YELLOW + "                                               THANK YOU")
        except Exception as exception:
            print(exception)
    else:
        print('File is missing')


main()
