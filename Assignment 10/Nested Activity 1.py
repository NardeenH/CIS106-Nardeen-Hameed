# A multiplication table:


def get_start():
    print("Enter Starting number")
    start = int(input())
    return start


def get_end():
    print("Enter Ending number")
    end = int(input())
    return end


def process_result(start, end):
    count = "  "
    for row in range(start, end + 1):
        count += str(row)+"   "
    count += "\n" 
    for row in range(start, end + 1):
        count += str(row) + "  "
        for column in range(start, end + 1):
            count += str(row * column) + "  "
        count += "\n"    
    return count


def get_result(count):
    print(count)
    return count

    
def main():
    start = get_start()
    end = get_end()
    count = process_result(start, end)
    get_result(count)


main()
