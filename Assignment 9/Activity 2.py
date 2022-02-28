# Create a program that asks the user to enter grade:


def get_number():
    print("Enter Number of score")
    number = int(input())        
    return number


def get_score():
    score = float(input())
    return score


def while_loop(number):
    total = 0
    count = 0
    while count < number:
        print("Score" + str(count+ 1) + ":")
        score = float(input())
        total = total + score
        count = count + 1
    average = total / number
    average_result(average)
    return total / number
    
 
def average_result(average):
    print("The average of the score is:" + str(average))
    return average
    

def main():
    number = get_number()
    while_loop(number)
    
    
main()
