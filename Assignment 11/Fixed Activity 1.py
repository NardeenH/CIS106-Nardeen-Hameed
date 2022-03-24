# Fixed Activity


def get_grade():
    print('How many grade you want to put')
    grade = int(input())
    return grade

def get_RealScore(x):
    print("Enter score" + str(x + 1) + ":");
    score = float(input())
    return score

def for_array():
    total = 0
    average = 0
    score = [-1] * grade
    for i in range(grade):
      score[i] = int(flout('Enter score' + str(x + 1) + ':'))
      average = avergae + score[i]
    return score
    
def get_hight():
    hight = score[0]
    low = score[0]
    for i in range (grade):
        if (score[i] > hight):
            hight = score[i]
    return hight

def get_low():
    for i in range(grade):
        if (score[i] < low):
            low = score[i]
    return low

def display_result(average):
        avrege = average/ grade
        return average
    
    
def main():
    grade = get_grade()
    print('The highest grade is:', hight)
    print('The lowest grade is:', low)
    print('The average grade is:', average)
    
main()
    



    



