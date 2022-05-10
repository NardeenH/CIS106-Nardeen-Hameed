def read_file(filename):
    array = []
    with open(filename, 'r') as file:
        for line in file:
            if line.find("TITLE") == -1:
                continue
            line = line.replace("<TITLE>", "")
            array.append(line)
    return array


def main():
    filename = "cd_catalog.xml"
    titles = read_file(filename)
    print(titles)


main()
