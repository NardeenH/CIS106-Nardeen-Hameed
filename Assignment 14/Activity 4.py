# Assignment 14, Activity 4  
    
    
def read_file(filename):
    block = []
    item = []
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            if line != "":
                item.append(line)
            else:                
                block.append(item)
                item = []      
        file.close()
    return block
        
        
def process_line(line):
    firstname = line[0].split()[0]
    lastname = line[0].split()[1]
    address = line[1]
    city = line[2].split(",")[0]
    state = line[2].split(",")[1].split()[0]
    code = line[2].split(",")[1].split()[1]
    return "{0}, {1}, {2}, {3}, {4}, {5}".format(lastname,
            firstname, address, city, state, code)


def the_outline(text):
    print(text)
    

def main():
    filename = "addresses.txt"
    block = read_file(filename)    
    for line in block:
        text = process_line(line)
        the_outline(text)
  
        
main()
