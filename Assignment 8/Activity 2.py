#  Calculate and display the average for the entered scores. 
    

def get_grade():
    print("How many grade you woukd like to enter?")
    numgrade = int(input())
    return numgrade


def get_realscore(x):
    print("Enter score" + str(x + 1) + ":")
    score = float(input())
    return score


def for_loop(numgrade):
    total = 0
    for x in range(0, numgrade - 1 + 1, 1):
        score = get_realscore(x)
        total = total + score
    return total / numgrade


def display_result(avg):
    print("The average is:" + str())
    return avg
    
     
def main():
    numgrade = get_grade()    
    avg = for_loop(numgrade)
    print("The average is:" + str(avg))
    

main()
