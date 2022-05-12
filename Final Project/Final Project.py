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
    title = []
    artist = []
    country = []
    price = []
    year = []
    for item in xml.iter('CD'):
        title.append(item.find('TITLE').text)
        artist.append(item.find('ARTIST').text)
        country.append(item.find('COUNTRY').text)
        price.append(item.find('PRICE').text)
        year.append(item.find('YEAR').text)
    items.append(title)
    items.append(artist)
    items.append(country)
    items.append(price)
    items.append(year)    
    return items


def calcalate_average(items):
    total = 0
    count = 0
    for index in range(len(items[0])):
        total = total + float(items[3][index])
        count = count + 1
    return (count, total / count)


def display_output(items):
    print("%-0s %-s %-0s %-s %-0s %-s %-0s %-s %-0s" %
          ("Title", " - ", 'Artist',
           " - ", 'Country',
           " - ", 'Price', " - ", 'Year'))
    for index in range(len(items[0])):
        print("%-0s %-s %-0s %-s %-0s %-s %-0s %-s %-0s" % (
              items[0][index], " - ",
              items[1][index], " - ",
              items[2][index], " - ", 
              items[3][index], " - ",
              items[4][index]))
    
    
def main():
    filename = "cd_catalog.xml"
    if os.path.isfile(filename):
        try:
            xml = read_url(filename)
            items = process_item(xml)
            count, average = calcalate_average(items)
            display_output(items)
            print((" %d items, $%.2f average price.")
                  % (count, average))
            print('\x1b[1;32;40m'
                  + 'Professor Dave, You are the best prof I have ever met!'
                  + '\x1b[0m')
        except Exception as exception:
            print(exception)
    else:
        print('File is missing')


main()
