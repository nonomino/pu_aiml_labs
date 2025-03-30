import sys

def minimax(board, depth, is_max):
    winner = check_winner(board)
    if winner:
        return {'X': 10 - depth, 'O': depth - 10, 'draw': 0}[winner]
    moves = [i for i in range(9) if board[i] == ' ']
    scores = [minimax(board[:i] + ['X' if is_max else 'O'] + board[i+1:], depth + 1, not is_max) for i in moves]
    return max(scores) if is_max else min(scores)

def best_move(board):
    return max((i for i in range(9) if board[i] == ' '), key=lambda i: minimax(board[:i] + ['X'] + board[i+1:], 0, False))

def check_winner(board):
    for a, b, c in [(0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6)]:
        if board[a] == board[b] == board[c] != ' ': return board[a]
    return 'draw' if ' ' not in board else None

def print_board(board):
    print("\n".join(" | ".join(board[i:i+3]) for i in range(0, 9, 3)))
    print()

def main():
    board = [' '] * 9
    while True:
        print_board(board)
        if (winner := check_winner(board)):
            print(f"{'You win!' if winner == 'O' else 'Computer wins!' if winner == 'X' else 'It\'s a draw!'}")
            break
        if (move := input("Enter your move (0-8): ")) and board[int(move)] == ' ':
            board[int(move)] = 'O'
        else:
            print("Invalid move. Try again.")
            continue
        if not check_winner(board):
            board[best_move(board)] = 'X'

if __name__ == "__main__":
    main()
