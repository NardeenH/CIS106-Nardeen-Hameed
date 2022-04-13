# Assinment 12,
# If your programming language supports it,
# update the grade score program above to
# replace the static array with a dynamic array,
# and extend the array as each item is added to the array.
# Continue accepting scores until the user enters a negative value.


# def get_grade():
# print(" Enter your Scores, if you want to stop enter negative value.")
# grade = int(input())
# return grade


def get_score():
    print(" Enter Score, to end it enter negitve value:")
    score = int(input())
    return score


def get_scores(score):
    scores = []
    while True:
        score = get_score()
        if score >= 0:
            scores.append(score) 
        else:
            break
    return scores
    

def calculate_max(scores):
    maximum = scores[0]
    for i in range(len(scores)):
        if maximum < scores[i]:
            maximum = scores[i]
    return maximum


def calculate_min(scores):
    minimum = scores[0]
    for i in range(len(scores)):
        if minimum > scores[i]:
            minimum = scores[i]
    return minimum
    
    
def calculate_average(scores):
    total = 0
    for i in scores:
        total = total + i
    average = total / len(scores)
    return average
  
    
def display_result(maximum, minimum, average):
    print(" The Highest number is:  %d" % (maximum))
    print(" The lowest number is:  %d" % (minimum))
    print(" The average number is:  %f" % (average))
    
    
def main():
    score = get_score()    
    score = get_scores(score)
    maximum = calculate_max(score)
    minimum = calculate_min(score)
    average = calculate_average(score)
    display_result(maximum, minimum, average)
   
   
main()
    