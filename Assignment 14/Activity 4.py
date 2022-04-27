# Assignment 14, Activity 4  
    
    
def read_file(filename):
    blok= []
    item = []
    with open (filename, 'r') as file:
        
        for line in file:
            line = line.strip()
            if line != "":
                item.append(line)
            else:                
                blok.append(item)
                item = []
        blok.append(item)       
        file.close()
    return blok


def outline(text):
     print(text)
        
        
def process_line(line):
     firstname = line[0].split()[0]
     lastname = line[0].split()[1]
     address = line[1]
     city = line[2].split(",")[0]
     postal_code = line[2].split(",")[1]
     return "{0},{1},{2},{3},{4}".format(lastname, firstname, address, city, postal_code)
#      outline(lastname, firstname, address, city, postal_code)
    

def main():
    filename = "addresses.txt"
    blok = read_file(filename)    
    for line in blok:
        text = process_line(line)
        outline(text)
  
        
main()
