#  Calculate and display the average for the entered scores. 
    

def get_grade():
    print("How many grades you woukd like to enter?")
    numgrade = int(input())
    return numgrade


def get_realscore(x):
    print("Score" + str(x + 1) + ":")
    score = float(input())
    return score


def process_grades(number_of_grades):
    total = 0
    for count in range(0, number_of_grades - 1 + 1, 1):
        score = get_realscore(count)
        total = total + score
    return total / number_of_grades


def display_result(average):
    print("The average is:" + str(average))
    
     
def main():
    number_of_grades = get_grade()    
    average = process_grades(number_of_grades)
    display_result(average)
    

main()
