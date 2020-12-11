#James hooper
#11/13/2020 
#Tic Tac Toe

#***********************Variables**************************************

X = "x"
O = "o"
EMPTY = " "
TIE = "TIE"
NUM_SQUARES = 9

#**********************************************************************

#***********************Functions**************************************

def display_instruct():
    """Display game instructions. to use simply type (display_instruct())"""
    print("""
    Welcome to  Tic Tac Toe.
    You will make your move known by entering a number, 0 - 8.
    the number will correspond to the board postision a s illustrated:

                \t0 | 1 | 2
                \t---------
                \t3 | 4 | 5
                \t---------
                \t6 | 7 | 8

    The game will begin soon
""")

def next_turn(turn):
    """This function switches the turn in the game. to use (turn = next_turn(turn))"""
    if turn == X:
        return O
    else:
        return X

def pieces():
    """Determine if player or computer goes first. to use (computer,human = pieces())"""
    go_first = yes_no("Do you want to go first? (y/n)")
    if go_first == "y":
        print("\nTake your first move")
        human = X
        computer = O
    else:
        print("\nI will go first.")
        human = O
        computer = X
    return computer, human
    
def yes_no(question):
    """Ask a yes or no question and get back a yes or no answer. """
    response = None
    while response not in ("y","n","no","yes",):
        response = input(question).lower()
    return response

def ask_number(question, low, high):
    """ask for a number within a range. to use (answer - ask_numver(question,low,high))"""
    response = None
    while response not in range(low,high):
        response = int(input(question))
    return response

def new_board():
    """To creat an empty board to use = (new_board())"""
    board = []
    for square in range(NUM_SQUARES):
        board.append(EMPTY)
    return board

def display_board(board):
    """Display game board on screen. to use (display_board(board))"""
    print()
    print("\t",board[0],"|",board[1],"|",board[2])
    print("\t", "---------")
    print("\t",board[3],"|",board[4],"|",board[5])
    print("\t", "---------")
    print("\t",board[6],"|",board[7],"|",board[8])
    print()

def leagal_moves(board):
    moves = []
    for square in range(NUM_SQUARES):
        if board[square] == EMPTY:
            moves.append(square)
    return moves

def human_move(board,human):
    """Get human move. to use (move = human_move(board,human))"""
    legal = leagal_moves(board)
    move = None
    while move not in legal:
        move = ask_number("Where will you move? (0 - 8):",0,NUM_SQUARES)
        if move not in legal:
            print("\nThat square is already occupied, Choose another.\n")
    return move

def winner(board):
    """Determine the game winner."""
    WAYS_TO_WIN = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 4, 8), (2, 4, 6), (0, 3, 6), (2, 5, 8), (1, 4, 7))
    for row in WAYS_TO_WIN:
        if board[row[0]] == board[row[1]] == board[row[2]] != EMPTY:
            winner = board[row[0]]
            return winner
    if EMPTY not in board:
        return TIE
    return None

def computer_move(board,computer,human):
    """Make computer move"""
    cboard = board[:]
    BEST_MOVES = (4, 0, 2, 6, 8, 1, 3, 5, 7)
    print("I'm taking square", end=" ")
    # if computer can win, take that move
    for move in leagal_moves(board):
        cboard[move] = computer
        if winner(cboard) == computer:
            print(move)
            return move
        # done checking this move, undo it
        cboard[move] = EMPTY
        
    #if human can win, block that move
    for move in leagal_moves(board):
        cboard[move] = human
        if winner(cboard) == human:
            print(move)
            return move
        # done checking this move, undo it
        cboard[move] = EMPTY
        
    #since no one can win on the next move, pick best open square
    for move in BEST_MOVES:
        if move in leagal_moves(board):
            print(move)
            return move

#main Game
def main():
    display_instruct()
    turn = X
    computer,human = pieces()
    board = new_board()
    display_board(board)
    
    while not winner(board):
        if turn == human:
            move = human_move(board,human)
            board[move]=human
        else:
            move = computer_move(board, computer, human)
            board[move] = computer
        display_board(board)
        turn = next_turn(turn)
        
        
        
    win = winner(board)
        
    display_board(board)
    print(str(win),"Won!\n\n")
#**********************************************************************

main()


