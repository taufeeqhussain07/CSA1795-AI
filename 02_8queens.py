def is_safe(board, row, col):
    # Check if there is a queen in the same row
    if any(board[row]):
        return False

    # Check if there is a queen in the same column
    if any(row[col] for row in board):
        return False

    # Check if there is a queen in the same diagonal (left to right)
    if any(board[i][j] for i, j in zip(range(row, -1, -1), range(col, -1, -1))):
        return False

    # Check if there is a queen in the same diagonal (right to left)
    if any(board[i][j] for i, j in zip(range(row, -1, -1), range(col, len(board)))):
        return False

    return True

def solve_queens(board, row):
    if row == len(board):
        return True

    for col in range(len(board)):
        if is_safe(board, row, col):
            board[row][col] = 1

            if solve_queens(board, row + 1):
                return True

            board[row][col] = 0

    return False

def print_solution(board):
    for row in board:
        print(" ".join("Q" if cell else "." for cell in row))
    print()

if __name__ == "__main__":
    board_size = 8
    chess_board = [[0] * board_size for _ in range(board_size)]

    if solve_queens(chess_board, 0):
        print("One solution found:")
        print_solution(chess_board)
    else:
        print("No solution found.")
