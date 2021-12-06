def parse_data():
    foisk_array = [0] * 9
    with open('day6.txt') as file:
        for line in file:
            line = line.split(',')
            line = [int(i) for i in line]

    for each in line:
        foisk_array[each] += 1

    return foisk_array


def iterate_foisk(foisk_array):
    temp = foisk_array[0]
    for i in range(8):
        foisk_array[i] = foisk_array[i+1]
    foisk_array[8] = temp
    foisk_array[6] += temp

    return foisk_array


def run_task(number):
    if number == 1:
        time = 80
    else:
        time = 256

    foisk_array = parse_data()
    for i in range(time):
        line = iterate_foisk(foisk_array)

    count = 0
    for foisk in foisk_array:
        count += foisk

    print(f'Task {number}: {count}')


if __name__ == '__main__':
    run_task(1)
    run_task(2)
