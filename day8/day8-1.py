def parse_data(line, count):
    output = line.strip('\n').split(' | ')
    output = output[1].split(' ')
    for combination in output:
        if len(combination) == 2 or len(combination) == 3 or len(combination) == 4 or len(combination) == 7:
            count += 1
    return count


def read_file():
    count = 0
    with open('day8.txt') as file:
        for line in file:
            count = parse_data(line, count)
    print(count)


if __name__ == '__main__':
    read_file()