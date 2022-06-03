
player = -1
ai = 1
empty = 0
tie = 0
stillGoing = 2

board = [empty, empty, empty, empty, empty, empty, empty, empty, empty]

def validateTurn(board, turn):
    return 1

def minimax(board, isMaximising, turn):

    state = checkState(board, turn)

    if state != stillGoing:
        return checkState(board, 0)

    if isMaximising:
        bestScore = -99

        for i in range(len(board)):
            if board[i] != empty:
                continue
            
            board[i] = ai
            score = minimax(board, False, i)
            board[i] = empty
            bestScore = max(score, bestScore)

    else:
        bestScore = 99

        for i in range(len(board)):
            if board[i] != empty:
                continue
            
            board[i] = player
            score = minimax(board, True, i)
            board[i] = empty
            bestScore = min(score, bestScore)
                
    return bestScore

def checkState(board, turn):
    row = turn // 3

    col = turn % 3
    rowCheck = [row, row + 3, row + 6]
    colCheck = [col, col + 3, col + 6]
    diagCheck = [0, 4, 8]
    antidiagCheck = [2, 4, 6]

    #toCheck = [rowCheck, colCheck, diagCheck, antidiagCheck]

    toCheck = [[0, 1, 2],[3, 4, 5],[6, 7, 8],[0, 3, 6],[1, 4, 7],[2, 5, 8],[0, 4, 8],[2, 4, 6]]

    for i in range(len(toCheck)):
        if board[toCheck[i][0]] == board[toCheck[i][1]] and board[toCheck[i][0]] == board[toCheck[i][2]]:
            if board[toCheck[i][0]] == player:
                return player
            if board[toCheck[i][0]] == ai:
                return ai
            
    for square in board:
        if square == empty:
            return stillGoing
    return tie
    
def printBoard(board):

    # line1 = board[:3]
    # line2 = board[3:6]
    # line3 = board[6:9]

    # for i in range(4):
    #     toPrint = []
    #     if line1[0] == player:
    #         toPrint.append(nought[i])
    #     elif line1[0] == ai:
    #         toPrint.append(cross[i])
    #     else:
    #         toPrint.append(empty)
    #     toPrint.append(lineDivider)

    '''nought1 = " ---- "
    nought2 = "|    |"
    nought3 = "|    |"
    nought4 = " ---- "
    nought = [nought1, nought2, nought3, nought4]

    cross1 =  " \  / "
    cross2 =  "  \/  "
    cross3 =  "  /\  "
    cross4 =  " /  \ "
    cross = [cross1, cross2, cross3, cross4]

    empty = "      "

    lineDivider = "|"
    lineBreak = "--------------------"'''

    line1 = board[:3]
    line2 = board[3:6]
    line3 = board[6:9]

    lines = [line1, line2, line3]

    for line in lines:
        toPrint = ''
        for i in range(len(line)):
            if line[i] == player:
                toPrint += 'O'
            elif line[i] == ai:
                toPrint += 'X'
            elif line[i] == empty:
                toPrint += ' '
            if i < len(line) - 1:
                toPrint += '|'
        print(toPrint)
        print("-----")

def aiMove(board):
    bestScore = -1
    for i in range(len(board)):
        if board[i] != empty:
                continue
            
        board[i] = ai
        score = minimax(board, False, i)
        board[i] = empty

        if score > bestScore:
            bestScore = score
            bestMove = i
    
    return bestMove


while(True):
    printBoard(board)
    playerTurn = input("Make Turn: ")
    playerTurn = int(playerTurn)
    validateTurn(board, playerTurn)
    board[playerTurn] = player
    state = checkState(board, playerTurn)
    if state == player:
        print("YAY YOU WON")
        break
    elif state == ai:
        print("AHAHAH SUCK IT ")
        break
    elif state == tie:
        print("DRAW")
        break

    printBoard(board)
    aiTurn = aiMove(board)

    board[aiTurn] = ai
    state = checkState(board, aiTurn)
    if state == player:
        print("YAY YOU WON")
        break
    elif state == ai:
        print("AHAHAH SUCK IT ")
        break
    elif state == tie:
        print("DRAW")
        break