class Submarine:
    def __init__(self):
        self.depth = 0
        self.horizontal_pos = 0
        self.aim = 0

    def forward(self, amount):
        self.horizontal_pos += amount
        self.depth += self.aim * amount

    def up(self, amount):
        self.aim -= amount

    def down(self, amount):
        self.aim += amount

    def solve(self):
        return self.depth * self.horizontal_pos


def parse_data(submarine, filename):
    with open(filename) as f:
        for line in f:
            instruction = line.split(' ')[0]
            amount = int(line.split(' ')[1])
            if instruction == 'up':
                sub.up(amount)
            elif instruction == 'down':
                sub.down(amount)
            else:
                sub.forward(amount)

if __name__ == '__main__':
    sub = Submarine()
    parse_data(sub, 'day2.txt')
    print('Task 2:', sub.solve())
