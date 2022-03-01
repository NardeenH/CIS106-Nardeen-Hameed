# Find the average of scores:


def get_number():
    print("Enter Number of scores")
    number = int(input())        
    return number


def get_score(count):
    print("score" + str(count + 1) + ":")
    score = float(input())
    return score


def while_loop(number_of_grade):
    total = 0
    count = 0
    while count < number_of_grade:
        print("Score" + str(count + 1) + ":")
        score = float(input())
        total = total + score
        count = count + 1
    average = total / number_of_grade
    average_result(average)
    return total / number_of_grade
    
 
def average_result(average):
    print("The average of the score is:" + str(average))
    

def main():
    number = get_number()
    while_loop(number)
    
    
main()
