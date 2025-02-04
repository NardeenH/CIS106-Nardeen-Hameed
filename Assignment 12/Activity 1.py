# Assinment 12,
# If your programming language supports it,
# update the grade score program above to
# replace the static array with a dynamic array,
# and extend the array as each item is added to the array.
# Continue accepting scores until the user enters a negative value.


def get_score():
    print(" Enter Score, to end it enter negitve value:")
    score = int(input())
    return score


def get_scores():
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
    print(f"The Highest number is: {maximum}")
    print(f"The lowest number is: {minimum}")
    print(f"The average number is: {average}")
    
    
def main():    
    score = get_scores()
    maximum = calculate_max(score)
    minimum = calculate_min(score)
    average = calculate_average(score)
    display_result(maximum, minimum, average)
    
     
main()
    
