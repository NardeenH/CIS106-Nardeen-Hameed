def displayResult(average):
    print(" The average is:" + str(average))
    
    return average

def doLoop(total, count):
    while True:    #This simulates a Do Loop
        grade = getGrade()
        total = total + grade
        count = count + 1
        if not(0 <= grade): break   #Exit loop
    total = total - grade
    average = float(total) / (count - 1)
    displayResult(average)
    
    return total

def getGrade():
    print(" Enter your Grade, if you want to stop enter negative value.")
    grade = int(input())
    
    return grade

# Main
# Review MathsIsFun: Definition of Average. Create a program that asks the user to enter grade scores. Use a loop to request each score and add it to a total. Continue accepting scores until the user enters either a negative value or no value (your choice). Finally, calculate and display the average for the entered scores.
total = 0
count = 0
doLoop(total, count)
