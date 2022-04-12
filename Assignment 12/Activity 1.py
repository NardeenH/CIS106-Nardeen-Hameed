# Assinment 12,
# If your programming language supports it,
# update the grade score program above to
# replace the static array with a dynamic array,
# and extend the array as each item is added to the array.
# Continue accepting scores until the user enters a negative value.


def get_grade():
    print('Enter score, to stop enter negitve value:')
    grade = int(input())
    return grade


def get_score():
    print(" Enter Score:")
    score = int(input())
    return score


def get_scores(grade):
    grades = []
    while True:
        grades.append(get_score())
        if grade <= 0:
            break
    return grades
    

def calculate_max(array):
    maximum = array[0]
    for i in range(len(array)):
        if maximum < array[i]:
            maximum = array[i]
    return maximum


def calculate_min(array):
    minimum = array[0]
    for i in range(len(array)):
        if minimum > array[i]:
            minimum = array[i]
    return minimum
    
    
def calculate_average(array):
    total = 0
    for i in range(len(array)):
        total = total + array[i]
    average = total / int(array[i])
    return average
  
    
def display_result(maximum, minimum, average):
    print(" The Highest number is:  %d" % (maximum))
    print(" The lowest number is:  %d" % (minimum))
    print(" The average number is:  %f" % (average))
    
    
def main():
    grade = get_grade()
    score = get_scores(grade)
    maximum = calculate_max(score)
    minimum = calculate_min(score)
    average = calculate_average(score)
    display_result(maximum, minimum, average)
   
   
main()
    