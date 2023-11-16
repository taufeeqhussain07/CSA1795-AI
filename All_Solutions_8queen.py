def print_solution(board):
    for row in board:
        print(" ".join(row))
    print()

def is_safe(board, row, col, n):
    # Check if there is a queen in the same row
    for i in range(col):
        if board[row][i] == 'Q':
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 'Q':
            return False

    # Check lower diagonal on left side
    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 'Q':
            return False

    return True

def solve_n_queens_util(board, col, n):
    if col == n:
        print_solution(board)
        return 1

    count = 0
    for i in range(n):
        if is_safe(board, i, col, n):
            board[i][col] = 'Q'

            count += solve_n_queens_util(board, col + 1, n)

            board[i][col] = '.'  # backtrack

    return count

def solve_n_queens(n):
    board = [['.' for _ in range(n)] for _ in range(n)]
    count = solve_n_queens_util(board, 0, n)

    if count == 0:
        print("No solution exists.")
    else:
        print(f"Total solutions: {count}")

if __name__ == "__main__":
    n = 8  # You can change this to solve the problem for different board sizes
    solve_n_queens(n)
