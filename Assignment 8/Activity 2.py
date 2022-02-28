#  Calculate and display the average for the entered scores. 
    

def get_grade():
    print("How many grades you woukd like to enter?")
    numgrade = int(input())
    return numgrade


def get_realscore(count):
    print("Score" + str(count + 1) + ":")
    score = float(input())
    return score


def process_grades(number_of_grades):
    total = 0
    for count in range(number_of_grades):
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
