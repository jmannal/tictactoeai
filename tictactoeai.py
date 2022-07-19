# Constant values
player = -1
ai = 1
empty = 0
draw = 0
stillGoing = 2
maxVal = 9
infinity = 10 # The best possible score is 9, thus 10 is a suitable number to
              # represent infinity
              
numbers = '012345678'
valid = 1
invalid = 0

# Validate turn
def validateTurn(board, turn):

    # The turn must be of a valid index (0-8)
    if turn < 0 or turn > 8:
        return invalid

    # This square must be empty
    if board[turn] != empty:
        return invalid
    return valid

# Implementation of minimax,
# The 'brains' of the program
def minimax(board, isMaximising, turn, depth):

    # Evaluate the state of the game
    state = checkState(board, turn)

    # Check if an end state has been reached
    if state != stillGoing:
        if state == ai:
            return maxVal - depth
        elif state == player:
            return -maxVal + depth
        else:
            return state

    if isMaximising:
        bestScore = -infinity

        for move in range(len(board)):
            if not validateTurn(board, move):
                continue
            
            # Update board with new move
            board[move] = ai

            # This player is the maximising player, so the next move player 
            # will be minimising
            score = minimax(board, False, move, depth + 1)

            # Remove board update
            board[move] = empty

            # The best score is the higher value of the current score and 
            # the best score because this player is the maximising player
            bestScore = max(score, bestScore)

    else:
        bestScore = infinity

        for move in range(len(board)):
            if not validateTurn(board, move):
                continue
            
            # Update board with new move
            board[move] = player

            # This player is the minimising player, so the next move player 
            # will be maximising
            score = minimax(board, True, move, depth + 1)

            # Remove board update
            board[move] = empty

            # The best score is the lower value of the current score and 
            # the best score because this player is the minimising player
            bestScore = min(score, bestScore)
                
    return bestScore

# Checks if there is a winner, draw, or if the game is still in progress
def checkState(board, turn):
    
    # All possible combinations that win TicTacToe
    c = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], 
               [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    
    # If the first square in each combination is the same as the second
    # and third, and they are not empty squares, someone has won
    for i in range(len(c)):
        if board[c[i][0]] == board[c[i][1]] \
        and board[c[i][0]] == board[c[i][2]]:
            if board[c[i][0]] != empty:
                return board[c[i][0]]
            
    # If the board is full and noone has one, it is a draw
    for square in board:
        if square == empty:
            return stillGoing

    return draw
    
# Prints the board
def printBoard(board):

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

# Generates the AI's move
def aiMove(board):
    bestScore = -1

    for move in range(len(board)):
        if not validateTurn(board, move):
            continue
        
        # Update board with new move
        board[move] = ai
        score = minimax(board, False, move, depth = 1)

        # Remove board update
        board[move] = empty

        # If this move is better than all the ones before it, it becomes
        # the best move
        if score > bestScore:
            bestScore = score
            bestMove = move
    
    return bestMove

# When an end state is reached, this function prints the result and exits the 
#program
def evaluateState(state):
    if state == stillGoing:
        return
    if state == player:
        print("You Win")
    if state == ai:
        print("You Lose")
    if state == draw:
        print("Draw")
    exit()

# Gets player choice of turn, provides all validity checks as well
def getPlayerTurn(board):
    turn = input("Make Turn: ")

    # Check input is a number
    if turn not in numbers:
        print("Enter number between 0-8 that is available")
        return getPlayerTurn(board)

    turn = int(turn)
    
    # Check input is a number between 0-8 and is an availalble square
    if not validateTurn(board, turn):
        print("Enter number between 0-8 that is available")
        return getPlayerTurn(board)

    return turn

# Game Loop
def gameLoop(board):

    while(True):
        # Get player turn
        playerTurn = getPlayerTurn(board)
        board[playerTurn] = player

        # Evaluate Player turn
        state = checkState(board, playerTurn)
        evaluateState(state)

        # Get AI turn
        aiTurn = aiMove(board)
        board[aiTurn] = ai
        printBoard(board)

        # Evaluate AI turn
        state = checkState(board, aiTurn)
        evaluateState(state)

def main():
    board = [empty, empty, empty, empty, empty, empty, empty, empty, empty]
    printBoard(board)

    gameLoop(board)

main()