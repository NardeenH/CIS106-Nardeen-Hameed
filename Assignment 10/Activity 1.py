def displayResult(average):
    print(" The average is:" + str(average))
    
    return average

def displayTotal(total, grade):
    total = total - grade

def doLoop(total, count):
    while True:    #This simulates a Do Loop
        print(" Enter your Grade, if you want to stop enter negative value.")
        grade = int(input())
        total = total + grade
        count = count + 1
        if not(0 <= grade): break   #Exit loop
    displayTotal(total, grade)
    average = float(total) / (count - 1)
    displayResult(average)
    
    return total

def getCount():
    count = 0
    
    return count

def getTotal():
    total = 0
    
    return total

# Main
# Review MathsIsFun: Definition of Average. Create a program that asks the user to enter grade scores. Use a loop to request each score and add it to a total. Continue accepting scores until the user enters either a negative value or no value (your choice). Finally, calculate and display the average for the entered scores.
total = getTotal()
count = getCount()
doLoop(total, count)
