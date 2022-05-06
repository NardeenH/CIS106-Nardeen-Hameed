# https://www.youtube.com/watch?v=rFxXDO8-keg
# Final Project:
# Some help from Tim for line 30.

import urllib.request
import xml.etree.ElementTree as ET


def read_url(filename):   
    xml = ET.parse(filename)
    return xml


def process_item(xml): 
    items = []
    for item in xml.iter('CD'):
        items.append({
            "title" : item.find('TITLE').text,
            "artist": item.find('ARTIST').text,
            "country": item.find('COUNTRY').text,
            "price": item.find('PRICE').text,
            "year": item.find('YEAR').text
            })
    return items


def calcalate_average(items):
    total = 0
    count = 0
    print("Title" + " - " + 'Artist' + " - " + 'Country' + " - " + 'Price' + " - " + 'Year')
    for element in items:
        print(element['title'] + " - " + element['artist'] + " - " +
              element['country'] + " - " + element['price'] + " - " + element['year'])
        total = total + float(element['price'])
        count = count + 1
    return (count, total /count)
     
    
def main():  
    filename = "cd_catalog.xml"
    xml = read_url(filename)
    items = process_item(xml)
    count,avr = calcalate_average(items)
    print(("%d items, $%.2f average price.")%(count,avr))


main()
