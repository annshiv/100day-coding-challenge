# -------Global variables -------

#board
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

# if game is still going
game_still_playing = True

# who won? or tie?
winner = None

# Who turn is this?
current_player = "X"

#display board
def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])

#play game
def play_game():
    # Display initial board
    display_board()
    while game_still_playing:
        handle_turn(current_player)

        check_if_game_over()

        flip_player()
    
    #if game has ended
    if winner == "X" or winner == "O":
        print(winner + " won.")
    elif winner == None:
        print("Tie.")

#handle turn
def handle_turn(player):

    print(player +"'s turn.")
    position = int(input("Choose a position from 1-9: ")) - 1
    valid = False
    while not valid:
        while position not in [0,1,2,3,4,5,6,7,8]:
            position = int(input("Choose a position from 1-9: ")) - 1
        if board[position] == "-":
            valid = True
        else:
            print("you can't go there. Go again")
            position = int(input("Choose a position from 1-9: ")) - 1
    
    board[position] = player
    display_board()


#check win
def check_if_game_over():
    check_if_win()

def check_if_win():

    global winner

    row_winner = check_rows()
    colum_winner = check_columns()
    diagonal_winner = check_diagonals()

    if row_winner:
        winner = row_winner
    elif colum_winner:
        winner = colum_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None

#check rows
def check_rows():
    global game_still_playing

    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"
    
    if row_1 or row_2 or row_3:
        game_still_playing = False
    
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]

#check columns
def check_columns():
    global game_still_playing

    column_1 = board[0] == board[3] == board[6] != "-"
    column_2 = board[1] == board[4] == board[7] != "-"
    column_3 = board[2] == board[5] == board[8] != "-"
    
    if column_1 or column_2 or column_3:
        game_still_playing = False
    
    if column_1:
        return board[0]
    elif column_2:
        return board[3]
    elif column_3:
        return board[6]

#check diagonals
def check_diagonals():
    global game_still_playing

    diagonal_1 = board[0] == board[4] == board[8] != "-"
    diagonal_2 = board[2] == board[4] == board[6] != "-"
    
    if diagonal_1 or diagonal_2:
        game_still_playing = False
    
    if diagonal_1:
        return board[0]
    elif diagonal_2:
        return board[2]

#flip player
def flip_player():
    global current_player

    if current_player == "X":
        current_player = "O"
    elif current_player == "O":
        current_player = "X"

play_game()