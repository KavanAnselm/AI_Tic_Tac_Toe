import random

# Constants
PLAYER_X = 'X'
PLAYER_O = 'O'
EMPTY = ' '

# Board
def print_board(board):
    print("\n")
    for row in range(3):
        print(" | ".join(board[row]))
        if row < 2:
            print("---------")
    print("\n")

def is_winner(board, player):
    for row in range(3):
        if all([cell == player for cell in board[row]]):
            return True
    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True
    if all([board[i][i] == player for i in range(3)]) or all([board[i][2 - i] == player for i in range(3)]):
        return True
    return False

def is_full(board):
    return all(board[row][col] != EMPTY for row in range(3) for col in range(3))

def minimax(board, depth, is_maximizing, alpha, beta):
    if is_winner(board, PLAYER_X):
        return 10 - depth
    if is_winner(board, PLAYER_O):
        return depth - 10
    if is_full(board):
        return 0
    
    if is_maximizing:
        max_eval = float('-inf')
        for row in range(3):
            for col in range(3):
                if board[row][col] == EMPTY:
                    board[row][col] = PLAYER_X
                    eval = minimax(board, depth + 1, False, alpha, beta)
                    board[row][col] = EMPTY
                    max_eval = max(max_eval, eval)
                    alpha = max(alpha, eval)
                    if beta <= alpha:
                        break
        return max_eval
    else:
        min_eval = float('inf')
        for row in range(3):
            for col in range(3):
                if board[row][col] == EMPTY:
                    board[row][col] = PLAYER_O
                    eval = minimax(board, depth + 1, True, alpha, beta)
                    board[row][col] = EMPTY
                    min_eval = min(min_eval, eval)
                    beta = min(beta, eval)
                    if beta <= alpha:
                        break
        return min_eval

def best_move(board):
    best_val = float('-inf')
    move = None
    for row in range(3):
        for col in range(3):
            if board[row][col] == EMPTY:
                board[row][col] = PLAYER_X
                move_val = minimax(board, 0, False, float('-inf'), float('inf'))
                board[row][col] = EMPTY
                if move_val > best_val:
                    best_val = move_val
                    move = (row, col)
    return move

def player_move(board):
    while True:
        try:
            move = int(input("Enter your move (1-9): "))
            if move < 1 or move > 9:
                print("Invalid move. Enter a number between 1 and 9.")
                continue

            row, col = (move - 1) // 3, (move - 1) % 3

            if board[row][col] == EMPTY:
                board[row][col] = PLAYER_O
                break
            else:
                print("Cell is already taken. Try again.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 9.")

def ai_move(board):
    print("AI is making its move...")
    row, col = best_move(board)
    board[row][col] = PLAYER_X

def play_game():
    board = [[EMPTY] * 3 for _ in range(3)]
    print_board(board)
    
    while True:
        # Player move
        player_move(board)
        print_board(board)
        if is_winner(board, PLAYER_O):
            print("Player O (You) wins!")
            break
        if is_full(board):
            print("It's a tie!")
            break

        # AI move
        ai_move(board)
        print_board(board)
        if is_winner(board, PLAYER_X):
            print("AI (Player X) wins!")
            break
        if is_full(board):
            print("It's a tie!")
            break

# Main game loop
if __name__ == "__main__":
    play_game()
