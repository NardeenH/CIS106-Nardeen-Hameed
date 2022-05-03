#  First hour-Checking the file if anything alright. 
with open("cd_catalog.xml.text", "r") as file:
    line = file.readlines()
    print(line)