


# Function to check if the current player has won
def check_win(board, player):
    # Check rows, columns, and diagonals for a win
   for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True
   if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
   return False

# Function to check if the board is full
def is_board_full(board):
    return all(board[i][j] != ' ' for i in range(3) for j in range(3))

# Depth-First Search function
def dfs(board, player):
    if check_win(board, 'X'):  # If X wins
        return 1
    elif check_win(board, 'O'):  # If O wins
        return -1
    elif is_board_full(board):  # If it's a tie
        return 0

    scores = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = player
                if player == 'X':
                    scores.append(dfs(board, 'O'))
                else:
                    scores.append(dfs(board, 'X'))
                board[i][j] = ' '

    if player == 'X':
        return max(scores)
    else:
        return min(scores)

# Function to find the best move using DFS
def find_best_move(board):
    best_score = float('-inf')
    best_move = None

    # Loop through all empty cells
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                # Make a move
                board[i][j] = 'X'
                # Call DFS to evaluate the score for this move
                score = dfs(board, 'O')
                # Backtrack
                board[i][j] = ' '
                # Update best move and score
                if score > best_score:
                    best_score = score
                    best_move = (i, j)

    return best_move

# Function to print the board
def print_board(board):
    for row in board:
        print(' | '.join(row))
        print('-' * 5)

# Initialize the Tic Tac Toe board
board = [[' ' for _ in range(3)] for _ in range(3)]

# Main game loop
while True:
    print_board(board)
    x, y = map(int, input("Enter your move (row and column separated by space): ").split())
    if board[x][y] != ' ':
        print("Invalid move! Try again.")
        continue
    board[x][y] = 'O'
    if check_win(board, 'O'):
        print("Congratulations! You win!")
        break
    if is_board_full(board):
        print("It's a tie!")
        break
    print("Computer is making a move...")
    best_move = find_best_move(board)
    board[best_move[0]][best_move[1]] = 'X'
    if check_win(board, 'X'):
        print_board(board)
        print("Computer wins!")
        break
    if is_board_full(board):
        print("It's a tie!")
        break
