#

import urllib.request
import xml.etree.ElemenTree

def read_file(filename):
    try:
        page = urllib.request.urlopen(filename).read().decode()
    except Exception as exception:
        print(str(exception) + " reading " + filename)
        exit(1)
for line in page.split("\n"):
    print(line)
    

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


main()
