import random
import math


def playerMove():
    print("Player Turn")
    check = False
    while check == False:
        x = input("Enter a move: ")
        check = available(int(x))

    board[int(x)] = 'X'


def computerMove(tmp):
    print("Computer Turn")
    if tmp == 1:
        x = random.randint(1, 9)
        board[x] = 'O'
    else:
        bestScore = -math.inf
        bestMove = None
        for i in range(1, 10):
            if available(i):
                board[i] = 'O'
                score = minimax()
                board[i] = '_'
                if score > bestScore:
                    bestScore = score
                    bestMove = i
        board[bestMove] = 'O'


def minimax():
    result = terminal()
    if result != None:
        return result

    bestScore = -math.inf
    for i in range(1, 10):
        if available(i):
            board[i] = 'O'
            score = minimax()
            board[i] = '_'
            bestScore = max(score, bestScore)
    return bestScore


def terminal():
    for x in range(1, 10):
        # checking rows & columns
        if x == 1 and board[x] == board[x + 1] == board[x + 2] and board[x] == 'O':
            return 1
        elif x == 1 and board[x] == board[x + 1] == board[x + 2] and board[x] == 'X':
            return -1
        if x == 1 and board[x] == board[x + 3] == board[x + 6] and board[x] == 'O':
            return 1
        elif x == 1 and board[x] == board[x + 3] == board[x + 6] and board[x] == 'X':
            return -1
        if x == 1 and board[x] == board[x + 4] == board[x + 8] and board[x] == 'O':
            return 1
        elif x == 1 and board[x] == board[x + 4] == board[x + 8] and board[x] == 'X':
            return -1
        if x == 2 and board[x] == board[x + 3] == board[x + 6] and board[x] == 'O':
            return 1
        elif x == 2 and board[x] == board[x + 3] == board[x + 6] and board[x] == 'X':
            return -1
        if x == 3 and board[x] == board[x + 2] == board[x + 4] and board[x] == 'O':
            return 1
        elif x == 3 and board[x] == board[x + 2] == board[x + 4] and board[x] == 'X':
            return -1
        if x == 3 and board[x] == board[x + 3] == board[x + 6] and board[x] == 'O':
            return 1
        elif x == 3 and board[x] == board[x + 3] == board[x + 6] and board[x] == 'X':
            return -1
        if x == 4 and board[x] == board[x + 1] == board[x + 2] and board[x] == 'O':
            return 1
        elif x == 4 and board[x] == board[x + 1] == board[x + 2] and board[x] == 'X':
            return -1
        if x == 7 and board[x] == board[x + 1] == board[x + 2] and board[x] == 'O':
            return 1
        elif x == 7 and board[x] == board[x + 1] == board[x + 2] and board[x] == 'X':
            return -1

    for x in board:
        if board[x] == '_':
            return  # ->board has empty spaces
    print("DRAW!")
    return 0


def available(var):
    if var > 0 and var < 10:
        if board[var] == '_':
            return True
    return False


def availableMoves():
    movesList = []
    for x in board:
        if board[x] == '_':
            movesList.append(x)
    return movesList


def startGame():
    tmp = 1
    while True:
        computerMove(tmp)
        tmp += 1
        printBoard()
        val = terminal()
        if val == 1:
            print("Computer Won!")
            exit()
        if val == -1:
            print("Player Won!")
            exit()
        if val == 0:
            print("DRAW!")
            exit()
        playerMove()
        printBoard()
        val = terminal()
        if val == 1:
            print("Computer Won!")
            exit()
        if val == -1:
            print("Player Won!")
            exit()
        if val == 0:
            print("DRAW!")
            exit()


def printBoard():
    for x in range(1, 10):
        print(board[x], end=" ")
        if x % 3 == 0:
            print('\n')


board = {1: '_', 2: '_', 3: '_', 4: '_', 5: '_', 6: '_', 7: '_', 8: '_', 9: '_'}
if __name__ == "__main__":
    printBoard()
    startGame()
