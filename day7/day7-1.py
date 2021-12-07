def parse_data():
    with open('day7.txt') as file:
        for line in file:
            input = line.strip('\n').split(',')
            input = [int(i) for i in input]

    start = min(input)
    stop = max(input)

    optimum = (float('inf'),0)

    for i in range(start, stop):
        fuel = 0
        for pos in input:
            fuel += abs(pos - i)
        if fuel < optimum[0]:
            optimum = (fuel, i)

    return optimum





if __name__ == '__main__':
    print(parse_data())
