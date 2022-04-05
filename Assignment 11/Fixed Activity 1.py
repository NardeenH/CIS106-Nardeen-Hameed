# Review MathsIsFun: Definition of Average.
# I get some help from Tim.


def get_grade():
    print('How many grade you want to put?')
    grade = int(input())
    return grade


def get_scores(grade):
    array = [None] * int(grade)
    for i in range(len(array)):
         array[i] = get_score()
    return array
  
    
def get_score():
    print("Enter score:")
    score = float(input())
    return score


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


def for_result(hight, low, average):
    print(" The Hight number is:  %d" % (hight))
    print(" The low number is:  %d" % (low))
    print(" The average number is:  %f" % (average))
    
    
def main():
    grade = get_grade()
    score = get_scores(grade)
    hight = calculate_high(score)
    low = calculate_low(score)
    average = calculate_avg(score)
    for_result(hight, low, average)
#     print(" The Hight number is:  %d" % (hight))
#     print(" The low number is:  %d" % (low))
#     print(" The average number is:  %f" % (average))


main()
