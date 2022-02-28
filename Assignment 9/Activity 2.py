# Create a program that asks the user to enter grade scores and find the average:


def get_number():
    print("Enter Number of score")
    number = int(input())        
    return number


def get_score():
    score = float(input())
    return score


def while_loop(number):
    count = 0
    total = 0
    while count < number:
        print("Enter Score")
        score = float(input())
        total = total + score
        count = count + 1
    average = total / number
    average_result(average)
    
 
def average_result(average):
    print("The average of the score is:" + str(average))
    

def main():
    number = get_number()
    total = 0
    count = 0
    while_loop(number)
    
    
main()
