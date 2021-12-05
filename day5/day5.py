import numpy as np
from scipy.sparse import csr_matrix
import matplotlib.pylab as plt



def parse_data(line):
    line = line.strip('\n')
    line = line.replace(' -> ', ',')
    line = line.split(',')
    line = [int(i) for i in line]
    return line


def add_points(points, board, task):
    x1,y1,x2,y2 = parse_data(points)
    if x2-x1 > 0:
        xdir = 1
    elif x2-x1 < 0:
        xdir = -1
    else:
        xdir = 0

    if y2-y1 > 0:
        ydir = 1
    elif y2-y1 < 0:
        ydir = -1
    else:
        ydir = 0

    if task == 1:
        if not ((xdir != 0) and (ydir != 0)):
            while not ((x1 == x2) and (y1 == y2)):
                board[x1][y1] += 1
                x1 += xdir
                y1 += ydir

            board[x2][y2] += 1
        return board
    else:
        while not ((x1 == x2) and (y1 == y2)):
            board[x1][y1] += 1
            x1 += xdir
            y1 += ydir

        board[x2][y2] += 1
        return board


if __name__ == '__main__':
    board = np.zeros((1000, 1000), dtype=int)
    task = 2
    with open('day5.txt') as file:
        for line in file:
            board = add_points(line, board, task)
            A = csr_matrix(board)

    temp = [((i, j), A[i,j]) for i, j in zip(*A.nonzero())]
    counter = 0
    for i in temp:
        if i[1] > 1:
            counter += 1


    print(counter)
