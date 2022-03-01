# Find the average of scores:


def get_number():
    print("Enter Number of scores")
    number = int(input())        
    return number


def get_realscore(count):
    print("score")
    score = float(input())
    return score


def while_loop(number):
    total = 0
    count = 0
    while count < number:
        print("Score")
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
