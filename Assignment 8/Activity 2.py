#  Calculate and display the average for the entered scores. 
    

def get_Grade():
    print("How many grade you woukd like to enter?");
    numgrade = int(input())
    return numgrade


def get_RealScore(x):
    print("Enter score" + str(x + 1) + ":");
    score = float(input())
    return score


def For_Loop(numgrade):
    total = 0
    for x in range(0, numgrade - 1 + 1, 1):
        score = get_RealScore(x)
        total= total + score
    return total/numgrade
    
     
def Main():
    numgrade=get_Grade()    
    avg = For_Loop(numgrade)
    print("The average is:" + str(avg));

Main()
