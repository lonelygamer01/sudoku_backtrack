import random
import os
import time

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
board = [[0 for x in range(9)] for y in range(9)]
solve = False

def print_board():
    if solve:
        time.sleep(0.2)
    else:
        time.sleep(0.05)
    os.system('cls||clear')
    for i in range(9):
        for j in range(9):
            print(board[i][j], end=" ")
        print()

def check_if_number_suitable(row, col, suit_number):
    # row
    if suit_number in board[row]:
        return False
    # column
    if suit_number in [board[i][col] for i in range(9)]:
        return False
    # 3x3 subgrid
    startRow = row - row % 3
    startCol = col - col % 3
    for i in range(3):
        for j in range(3):
            if board[startRow + i][startCol + j] == suit_number:
                return False
    return True

def solve_sudoku(row=0, col=0,):
    if row == 8 and col == 9:  # base case
        return True
    if col == 9:  #if last pos in a row move down
        row += 1
        col = 0
    if board[row][col] > 0:  # dont touch non 0 cells
        return solve_sudoku(row, col + 1)

    for num in numbers:
        if check_if_number_suitable(row, col, num):
            board[row][col] = num
            print_board()
            if solve_sudoku(row, col + 1):
                return True
        board[row][col] = 0  # fucked up, reverse
    return False


def generate_complete_sudoku():
    global numbers
    numbers = random.sample(numbers, len(numbers))
    solve_sudoku()
    remove_numbers_from_board(40)

def remove_numbers_from_board(count):
    while count > 0:
        row = random.randint(0, 8)
        col = random.randint(0, 8)
        if board[row][col] != 0:
            board[row][col] = 0
            count -= 1
    time.sleep(1)

generate_complete_sudoku()

solve = True
if solve_sudoku():
    print("Nice")
else:
    print("Shit happens.")
