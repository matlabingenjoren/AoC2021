def parse_line():
    task_output = 0
    with open('day8.txt') as file:
        for line in file:
            zero = set()
            one = set()
            two = set()
            three = set()
            four = set()
            five = set()
            six = set()
            seven = set()
            eight = set()
            nine = set()

            line = line.strip('\n')
            all_numbers = line.replace(' | ', ' ').split(' ')
            task_numbers = line.split(' | ')[1]
            task_numbers = task_numbers.split(' ')
            task_code = [set() for _ in range(4)]
            for y in range(4):
                [task_code[y].add(task_numbers[y][i]) for i in range(len(task_numbers[y]))]

            input_numbers = line.split(' | ')[0]
            input_numbers = input_numbers.split(' ')
            input_numbers = sorted(input_numbers, key=len)

            [one.add(input_numbers[0][i]) for i in range(len(input_numbers[0]))]
            [seven.add(input_numbers[1][i]) for i in range(len(input_numbers[1]))]
            [four.add(input_numbers[2][i]) for i in range(len(input_numbers[2]))]
            [eight.add(input_numbers[9][i]) for i in range(len(input_numbers[9]))]

            remaining_numbers = [set() for _ in range(6)]
            for y in range(6):
                [remaining_numbers[y].add(input_numbers[y+3][i]) for i in range(len(input_numbers[y+3]))]

        # if len(three) == 0:
            for i in range(3):
                if remaining_numbers[i] | one == remaining_numbers[i]:
                    three = remaining_numbers[i]
                    remaining_numbers.pop(i)
                    break

            if len(remaining_numbers[0] | four) == 6:
                five = remaining_numbers[0]
                two = remaining_numbers[1]
                remaining_numbers.pop(1)
                remaining_numbers.pop(0)
            else:
                five = remaining_numbers[1]
                two = remaining_numbers[0]
                remaining_numbers.pop(1)
                remaining_numbers.pop(0)

            for i in range(3):
                if len(remaining_numbers[i] | four) == 6:
                    nine = remaining_numbers[i]
                    remaining_numbers.pop(i)
                    break

            if len(remaining_numbers[0] | one) == 6:
                zero = remaining_numbers[0]
                six = remaining_numbers[1]
            else:
                zero = remaining_numbers[1]
                six = remaining_numbers[0]

            output_string = ''
            for i in range(4):
                if task_code[i] == zero:
                    output_string += '0'
                elif task_code[i] == one:
                    output_string += '1'
                elif task_code[i] == two:
                    output_string += '2'
                elif task_code[i] == three:
                    output_string += '3'
                elif task_code[i] == four:
                    output_string += '4'
                elif task_code[i] == five:
                    output_string += '5'
                elif task_code[i] == six:
                    output_string += '6'
                elif task_code[i] == seven:
                    output_string += '7'
                elif task_code[i] == eight:
                    output_string += '8'
                else:
                    output_string += '9'

            task_output += int(output_string)

    return task_output


if __name__ == '__main__':
    print(parse_line())
