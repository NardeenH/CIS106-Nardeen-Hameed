# https://www.youtube.com/watch?v=rFxXDO8-keg
# Final Project:
# Some help from Tim.
# https://thepythonguru.com/python-string-formatting/
# import urllib.request
# https://www.youtube.com/watch?v=rFxXDO8-keg
# Final Project:
# Some help from Tim.
# https://thepythonguru.com/python-string-formatting/
# import urllib.request


import xml.etree.ElementTree as ET
import os


def read_file(filename):   
    items = []
    with open(filename, 'r') as file:
        for line in file:
            if line.find("TITLE") ==-1:
                continue
            line = line.replace("<TITLE>","")
            line = line.replace("</TITLE>\n","")
            line = line.replace(" ","")
            
            items.append(line)
           
            
    print(items)              
    return items


def calcalate_average(items):
    total = 0
    count = 0

#     print("%-5s %-5s %-5s %-5s %-5s" %("Title",'Artist','Country','Price','Year'))
    for element in items:
        print("%-30s %-30s %-30s %-30s %-30s" %(element['title'],
              element['artist'], 
              element['country'], 
              element['price'],
              element['year']))
        total = total + float(element['price'])
        count = count + 1
    return (count, total / count)
     
    
def main():
    filename = "cd_catalog.xml"
    if os.path.isfile(filename):
        try:
            items = read_file(filename)
            count, average = calcalate_average(items)
            print((" %d items, $%.2f average price.") % (count, average))
        except Exception as exception:
            print(exception)
    else:
        print('File is missing')


main()