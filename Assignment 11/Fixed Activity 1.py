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
    print("Score " + str(count + 1) + ": ")
    score = float(input())
    return score


def calculate_high(score):
    height = score[0]
    for i in score:
        if (i > height):
            height = i
    return height


def calculate_low(score):
    low = score[0]
    for i in score:
        if (i < low):
            low = i
    return low


def calculate_average(score):
    total = 0
    for i in score:
        total = total + i
    average = total / len(score)
    return average


def display_result(height, low, average):
    print(" The high number is:  %d" % (height))
    print(" The low number is:  %d" % (low))
    print(" The average number is:  %f" % (average))
    
    
def main():
    grade = get_grade()
    score = get_scores(grade)
    height = calculate_high(score)
    low = calculate_low(score)
    average = calculate_average(score)
    display_result(height, low, average)


main()
