# Review MathsIsFun: Definition of Average.
# I get some help from Tim.


def get_grade():
    print('How many grades you want to put?')
    grade = int(input())
    return grade


def get_scores(grade):
    count = 0
    array = [None] * int(grade)
    for i in range(len(array)):
        array[i] = get_score(count)
        count = count + 1
    return array
  
    
def get_score(count):
    print("Score" + str(count + 1) + ": ")
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


def display_result(hight, low, average):
    print(" The Hight number is:  %d" % (hight))
    print(" The low number is:  %d" % (low))
    print(" The average number is:  %f" % (average))
    
    
def main():
    grade = get_grade()
    score = get_scores(grade)
    hight = calculate_high(score)
    low = calculate_low(score)
    average = calculate_avg(score)
    display_result(hight, low, average)
#     print(" The High number is:  %d" % (hight))
#     print(" The low number is:  %d" % (low))
#     print(" The average number is:  %f" % (average))


main()
