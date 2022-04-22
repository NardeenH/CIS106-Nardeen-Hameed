# Assignment14, Activity4

import os
import sys


def create_file(filename):
    try:
        with open(filename, "w") as file:
            for i in range(1):
                name = input("Enter your name: ")
                street = input("Enter your street name: ")
                town = input("Enter your town/city: ")
                county = input("Enter your county: ")
                postcode = input("Enter your postcode: ")
                
                file.append((name, street, town.strip(), county.strip(), postcode.strip()))
        print("Error creating", filename)
        print(sys.exc_info()[1])
        

def read_file(filename):
    try:
        with open(filename, "r") as file:
            line = file.read()
            for line in file:
                line = line.strip()
                print(line)
        print()
    except:
        print("error reading", filename)
        print(sys.exc_info()[1])
            
            
def output_file(file):
    for i in file:
        print(',').join(i)
        

              
def main():
    filename = "~file.txt"
    if os.path.isfile(filename):
        print("File alreaday exists.")
    else:
        create_file(filename)
        read_file(filename)
        output_file(file)

main()
    
    

    
    
    
