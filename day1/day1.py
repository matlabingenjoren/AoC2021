def uppg1(filename):
    previous_number = 0
    current_number = 0
    count = 0

    with open(filename) as f:
        for line in f:
            current_number = int(line.replace('\n', ''))
            if previous_number == 0:
                previous_number = current_number
                continue
            else:
                if current_number > previous_number:
                    count += 1

                previous_number = current_number

    return count


def uppg2(filename):
    current_number = 0
    number_buffer = [0, 0, 0]
    previous_set = 0
    current_set = 0
    count = 0

    with open(filename) as f:
        for line in f:
            current_number = int(line.replace('\n', ''))
            if number_buffer[2] == 0:
                number_buffer[2] = number_buffer[1]
                number_buffer[1] = number_buffer[0]
                number_buffer[0] = current_number

                continue
            else:
                number_buffer[2] = number_buffer[1]
                number_buffer[1] = number_buffer[0]
                number_buffer[0] = current_number

                current_set = number_buffer[0] + number_buffer[1] + number_buffer[2]
                if current_set > previous_set:
                    count += 1

                previous_set = current_set

    return count


if __name__ == '__main__':
    print('Uppg 1: ', uppg1('day1.txt'))
    print('Uppg 2: ', uppg2('day1.txt'))
