# Find it.

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
numgrade = getGrade()
total = 0
for count in range(0, numgrade - 1 + 1, 1):
    print("Enter grade" + str(count + 1) + ":")
    grade = float(input())
    total = total + grade
ava = total / numgrade
print(" The average is:" + str(ava))
