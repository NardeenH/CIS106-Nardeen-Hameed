# Assignment 14, Activity1


def file_read(filename):
    scores = []
    with open (filename, 'r') as file:
        item = 0
        for line in file:
            if item > 0:
                score = line.split(',')
                scores.append(int(score[1]))
            item += 1
        file.close()
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
    filename = "scores.txt"
    scores = file_read(filename)
    print(scores)
    maximum = calculate_max(scores)
    minimum = calculate_min(scores)
    average = calculate_average(scores)
    display_result(maximum, minimum, average)
    
    
main()
  