def parse_data():
    with open('day6test.txt') as file:
        for line in file:
            line = line.split(',')
            line = [int(i) for i in line]
    return line


def iterate_line(line):
    new_line = []
    for foisk in line:
        if foisk == 0:
            new_line.append(6)
            new_line.append(8)
        else:
            new_line.append(foisk-1)
    return new_line


if __name__ == '__main__':
    line = parse_data()
    for i in range(80):
        line = iterate_line(line)
    print(len(line))
