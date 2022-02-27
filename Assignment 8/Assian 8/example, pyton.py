def forLoop(grade, total, ava, numgrade):
    total = 0
    for count in range(0, numgrade - 1 + 1, 1):
        print("Enter grade" + str(count + 1) + ":")
        grade = float(input())
        total = total + grade
    ava = total / numgrade
    print(" The average is:" + str(ava))

def getGrade():
    print(" How many grade you would like to enter?")
    numgrade = int(input())
    
    return numgrade

def getRealGrade(count):
    print("Enter grade" + str(count + 1) + ":")
    
    return grade

# Main
# Review MathsIsFun: Definition of Average. Create a program that asks the user to enter grade scores. Start by asking the user how many scores they would like to enter. Then use a loop to request each score and add it to a total. Finally, calculate and display the average for the entered scores.
numgrade = getGrade()
total = 0
for count in range(0, numgrade - 1 + 1, 1):
    print("Enter grade" + str(count + 1) + ":")
    grade = float(input())
    total = total + grade
ava = total / numgrade
print(" The average is:" + str(ava))
