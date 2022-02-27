#  Calculate and display the average for the entered scores. 
    
def get_Grade():
    print("How many grade you woukd like to enter?")
    numgrade = int(input())
    return numgrade


def get_RealGrade(x):
    print("Enter grade" + str(x + 1) + ":")
    grade = float(input())
    return grade


def For_Loop(numgrade):
    total=0
    for x in range(0, numgrade - 1 + 1, 1):
        grade = get_RealGrade(x)
        total= total+grade
    return total/numgrade
    
    
    
def Main():
    numgrade=get_Grade()    
    ave = For_Loop(numgrade)
    print("The average is:" + str(ave))

Main()




