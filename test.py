'''
from sudoku_solver import solve


board = [
    [6, 0, 9, 0, 0, 4, 0, 0, 1],
    [8, 0, 0, 0, 5, 0, 0, 0, 0],
    [0, 3, 5, 1, 0, 9, 0, 0, 8],
    [0, 0, 8, 0, 0, 0, 0, 0, 4],
    [0, 5, 0, 0, 0, 0, 0, 3, 0],
    [4, 0, 0, 0, 7, 0, 0, 5, 2],
    [0, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 0, 4, 0, 0, 0, 0],
    [7, 6, 0, 9, 3, 0, 0, 0, 0]
]

solve(board)
for row in board:
    print(row)
'''

from sudoku_solver import solve
from tess import get_board

# board = get_board('download.png')
board = [
    [0, 0, 0, 0, 4, 0, 0, 0, 0],
    [0, 0, 0, 3, 0, 0, 0, 0, 9],
    [0, 8, 0, 0, 9, 1, 6, 5, 0],
    [1, 0, 0, 0, 0, 0, 0, 8, 0],
    [8, 2, 7, 0, 0, 0, 1, 4, 5],
    [0, 4, 0, 0, 0, 0, 0, 0, 2],
    [0, 6, 2, 7, 1, 0, 0, 3, 0],
    [9, 0, 0, 0, 0, 5, 0, 0, 0],
    [0, 0, 0, 0, 6, 0, 0, 0, 0]
]
for row in board:
    print(row)
solve(board)
print('-' * 10)
for row in board:
    print(row)