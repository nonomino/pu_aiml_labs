import pygame
import sys


def minimax(board, depth, is_max):
    winner = check_winner(board)
    if winner:
        return {'X': 10 - depth, 'O': depth - 10, 'draw': 0}[winner]

    moves = [i for i in range(9) if board[i] == ' ']
    if is_max:
        return max(minimax(board[:i] + ['X'] + board[i+1:], depth + 1, False) for i in moves)
    else:
        return min(minimax(board[:i] + ['O'] + board[i+1:], depth + 1, True) for i in moves)


def best_move(board):
    moves = [i for i in range(9) if board[i] == ' ']
    return max(moves, key=lambda i: minimax(board[:i] + ['X'] + board[i+1:], 0, False))


def check_winner(board):
    for a, b, c in [(0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6)]:
        if board[a] == board[b] == board[c] != ' ':
            return board[a]
    return 'draw' if ' ' not in board else None


def draw_board(screen, board):
    screen.fill((255, 255, 255))
    for x in range(1, 3):
        pygame.draw.line(screen, (0, 0, 0), (x * 100, 0), (x * 100, 300), 3)
        pygame.draw.line(screen, (0, 0, 0), (0, x * 100), (300, x * 100), 3)
    for i in range(9):
        if board[i] != ' ':
            font = pygame.font.Font(None, 80)
            text = font.render(board[i], True, (0, 0, 0))
            x, y = (i % 3) * 100 + 35, (i // 3) * 100 + 25
            screen.blit(text, (x, y))
    pygame.display.flip()


def show_message(screen, message):
    font = pygame.font.Font(None, 40)
    text = font.render(message, True, (0, 0, 0))
    screen.fill((255, 255, 255))
    screen.blit(text, (50, 130))
    pygame.display.flip()
    pygame.time.wait(2000)


def main():
    pygame.init()
    screen = pygame.display.set_mode((300, 300))
    pygame.display.set_caption("Tic Tac Toe")

    while True:
        board = [' '] * 9
        human_turn = True
        game_over = False

        while not game_over:
            draw_board(screen, board)
            winner = check_winner(board)
            if winner:
                if winner == 'X':
                    print("Computer (X) wins!")
                    show_message(screen, "You Lose!")
                elif winner == 'O':
                    print("Human (O) wins!")
                    show_message(screen, "You Win!")
                else:
                    print("Game is a draw!")
                    show_message(screen, "It's a Draw!")
                game_over = True
                break

            if human_turn:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        x, y = event.pos
                        index = (y // 100) * 3 + (x // 100)
                        if board[index] == ' ':
                            print(f"Human marked cell {index} with O")
                            board[index] = 'O'
                            human_turn = False
            else:
                pygame.time.wait(500)
                move = best_move(board)
                print(f"Computer marked cell {move} with X")
                board[move] = 'X'
                human_turn = True

        draw_board(screen, board)
        pygame.time.wait(1000)

        screen.fill((255, 255, 255))
        font = pygame.font.Font(None, 30)
        text1 = font.render("Press R to Restart", True, (0, 0, 0))
        text2 = font.render("Press Q to Quit", True, (0, 0, 0))
        screen.blit(text1, (60, 100))
        screen.blit(text2, (90, 150))
        pygame.display.flip()

        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        waiting = False
                    elif event.key == pygame.K_q:
                        pygame.quit()
                        sys.exit()


if __name__ == "__main__":
    main()
