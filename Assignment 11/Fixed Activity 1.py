# Fixed Activity


def get_grade():
    print('How many grade you want to put')
    grade = int(input())
    return grade


def get_score(i):
    print("Enter score" + str(i + 1) + ":")
    score = float(input())
    return score


def get_scores(i):
    total = 0
    for i in range(0, grade - 1 + 1, 1):
        score = get_Score(i)
        total= total + score
    return total/grade


def calculate_high():
    hight = score[0]
    low = score[0]
    for i in range (grade):
        if (score[i] > hight):
            hight = score[i]
    return hight


def calculate_low():
    for i in range(grade):
        if (score[i] < low):
            low = score[i]
    return low


def display_result(average):
        avrege = average/ grade
        return average
    
    
def main():
    grade = get_grade()
    print(grade)
    # score= get_score(i)
    # print('The highest grade is:', hight)
    # print('The lowest grade is:', low)
    # print('The average grade is:', average)


main()
