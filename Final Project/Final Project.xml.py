# Final

import urllib.request
import xml.etree.ElementTree as ET

def read_url(filename):   
    xml_page = ET.parse(filename)
    return xml_page


def process_item(xml_page): 
    items = []
    for item in xml_page.iter('CD'):
        items.append({"title" : item.find("TITLE").text})
        print("title","-","artist","-","company","-","country","-","price","-","year")
    for element in items:
        print((element['title'], element['artist'], element['country'], element['price'], element['year']))
    return items
#def read_file(filename):
  #  try:
   #     page = urllib.request.urlopen(filename).read().decode()
    #except Exception as exception:
     #   print(str(exception) + " reading " + filename)
      #  exit(1)
#for line in page.split("\n"):
 #   print(line)
    

# url = " https://www.w3schools.com/xml/cd_catalog.xml"
# page = urllib.request.urlopen(url).read()
# 



# with open("cd_catalog.xml", "r") as file:
#     line = file.read()
#     print(line)
#     
    


#
    
#  
# with open("cd_catalog.xml", "r") as file:
#     line = file.read()
#     
#     print(line)



# def read_file(filename):
#     with open(filename, 'r') as file:
#         for line in file:
#             print(line.strip())
# #         line = file.readlines()
#         return line
# 
#     
#     
#     
def main(): 
#     filename = "https://www.w3schools.com/xml/cd_catalog.xml"
    filename = "cd_catalog.xml"
    xml = read_url(filename)
    items = process_item(xml_page)


main()
