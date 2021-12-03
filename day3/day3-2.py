from copy import deepcopy

def parse_data():
    filename = 'day3.txt'
    ls = []

    with open(filename) as file:
        for line in file:
            line = line.strip('\n')
            ls += [line]

    return ls


def iterate(ls, gas, target_index):
    target = ''
    counter = 0
    delete = []

    for item in ls:
        if item[target_index] == '1':
            counter += 1

    if gas == 'oxygen':
        if counter >= len(ls)/2:
            target = '1'
        else:
            target = '0'

        for ind, each in enumerate(ls):
            if each[target_index] is not target:
                delete.append(ind)

        for each in reversed(delete):
            ls.pop(each)

    if gas == 'CO2':
        if counter >= len(ls)/2:
            target = '0'
        else:
            target = '1'

        for ind, each in enumerate(ls):
            if each[target_index] is not target:
                delete.append(ind)

        for each in reversed(delete):
            ls.pop(each)
    return ls


def solve(ls):
    ls_oxygen = deepcopy(ls)
    ls_CO2 = deepcopy(ls)
    target_index = 0
    while len(ls_oxygen) > 1:
        ls_oxygen = iterate(ls_oxygen, 'oxygen', target_index)
        target_index += 1

    target_index = 0
    while len(ls_CO2) > 1:
        ls_CO2 = iterate(ls_CO2, 'CO2', target_index)
        target_index += 1

    return int(ls_oxygen[0], base=2)*int(ls_CO2[0], base=2)

if __name__ == '__main__':
    ls = parse_data()
    result = solve(ls)
    print(f'Task 2 : {result}')

