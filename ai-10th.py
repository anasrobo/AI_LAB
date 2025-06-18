N = 8
def print_solution(board):
    for row in board:
        print("".join("Q" if col else "." for col in row))
        print("\n")
def is_safe(board, row, col, n):
    for i in range(row):
        if board[i][col]:
            return False

    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j]:
            return False
        i -= 1
        j -= 1

    i, j = row, col
    while i >= 0 and j < n:
        if board[i][j]:
            return False
        i -= 1
        j += 1

    return True
def solve_N_queens(board, row, n):
    if row == n:
        print_solution(board)
        print("\n--------------\n")
        return False

    result = False
    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1
            solve_N_queens(board, row + 1, n)
            board[row][col] = 0  # backtrack
    
def nQueens(n):
    board = [[0] * n for i in range(n)]
    if not solve_N_queens(board, 0, n):
        print("No Solution Exists")
    else:
        print("Solution Printed Above.")
nQueens(8)
