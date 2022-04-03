# Review MathsIsFun: Definition of Average.
# I get some help from Tim.
# I get some help from tutor.

def get_grade():
    print('How many grade you want to put?')
    grade = int(input())
    return grade


def grade_array(grade):
    array = [None] * int(grade)
    return array
  
    
def get_score():
    print("Enter score:")
    score = float(input())
    return score


def get_scores(grade):
    grades = []    
    for i in range(grade):
        grades.append(get_score())
    return grades


def calculate_high(score):
    hight = score[0]
    for i in score:
        if (i > hight):
            hight = i
    return hight


def calculate_low(score):
    low = score[0]
    for i in score:
        if (i < low):
            low = i
    return low


def calculate_avg(score):
    total = 0
    for i in score:
        total = total + i
    average = total / len(score)
    return average
    
    
def main():
    grade = get_grade()
    inputs = get_scores(grade)
    hight = calculate_high(inputs)
    low = calculate_low(inputs)
    average = calculate_avg(inputs)
    print(" The Hight number is:  %d" % (hight))
    print(" The low number is:  %d" % (low))
    print(" The average number is:  %f" % (average))
   
   
main()
