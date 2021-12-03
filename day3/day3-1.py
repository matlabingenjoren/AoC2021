def parse_data(linelength):
    filename = 'day3.txt'
    counter = [0] * linelength  # byt till hur långa siffrorna är
    length = 0
    with open(filename) as file:
        for line in file:
            line = line.strip('\n')
            length += 1
            for index, bit in enumerate(line):
                if bit == '1':
                    counter[index] += 1

    return counter, length


def solve(counter, length):
    gamma = ''
    epsilon = ''

    for amount in counter:
        if int(amount)/length > 0.5:
            gamma = gamma + '1'
            epsilon = epsilon + '0'
        else:
            gamma = gamma + '0'
            epsilon = epsilon + '1'

    gamma = int(gamma, base=2)
    epsilon = int(epsilon, base=2)

    return gamma*epsilon


if __name__ == '__main__':
    counter, length = parse_data(12)
    result = solve(counter, length)
    print(f'Task 1 : {result}')
