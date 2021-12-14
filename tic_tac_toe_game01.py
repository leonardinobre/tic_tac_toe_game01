from time import sleep

msg = """

A TIC TAC TOE GAME

This is a tic tac toe game!
The board has 9 positions, from 1 to 9.
You have to choose a position in the board not covered yet;
and it will put your mark on that position!
If you choose an already covered position, you will lose your turn!
If you choose a position, not on the board,
you may choose another position.

Let's play!
"""

print(msg)

sleep(1)


#----Global Variables----


# a board
board = ['-', '-', '-'
        ,'-', '-', '-'
        ,'-', '-', '-']

# game is still going
game_still_going = True

# Who won? or Tie?
winner = None

# current player
current_player = 'X'


# play game of tic tac toe
def play_game():

    handle_turn()
    display_board()
    flip_player()
    check_winner()


# display board
def display_board():

    print(board[0], "|", board[1], "|", board[2])
    print(board[3], "|", board[4], "|", board[5])
    print(board[6], "|", board[7], "|", board[8])

    print()


# handle a single turn of an arbitrary player
def handle_turn():

    print(f"It's {current_player}'s turn!")

    position = 0

    while position not in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:

        position = input("Choose a position from 1-9:  ")

    position = int(position) - 1

    if board[position] == '-':

           board[position] = current_player

    else:
        print(f'{current_player} lost its turn cause this position had already gone!!!')


def flip_player():

    global current_player

    if current_player == 'X':
        current_player = 'O'

    elif current_player == 'O':
        current_player = 'X'


def check_winner():

    global game_still_going

    check_rows()
    check_columns()
    check_diagonals()

    if winner == 'X' or winner == 'O':
        print(f'{winner} won!')
        game_still_going = False

    elif "-" not in board:
        print("Tie!")
        game_still_going = False


def check_rows():

    global winner

    row_1 = board[0] == board[1] == board[2] != '-'
    row_2 = board[3] == board[4] == board[5] != '-'
    row_3 = board[6] == board[7] == board[8] != '-'

    if row_1:
        row_winner = board[0]
    elif row_2:
        row_winner = board[3]
    elif row_3:
        row_winner = board[6]

    if row_1 or row_2 or row_3:
       winner = row_winner


def check_columns():

    global winner

    column_1 = board[0] == board[3] == board[6] != '-'
    column_2 = board[1] == board[4] == board[7] != '-'
    column_3 = board[2] == board[5] == board[8] != '-'

    if column_1:
        column_winner = board[0]
    elif column_2:
        column_winner = board[1]
    elif column_3:
        column_winner = board[2]

    if column_1 or column_2 or column_3:
       winner = column_winner


def check_diagonals():

    global winner

    diagonal_1 = board[0] == board[4] == board[8] != '-'
    diagonal_2 = board[2] == board[4] == board[6] != '-'


    if diagonal_1:
        diagonal_winner = board[0]
    elif diagonal_2:
        diagonal_winner = board[2]


    if diagonal_1 or diagonal_2:
       winner = diagonal_winner


while game_still_going:
    play_game()

else:
    print('GAME OVER!')
    print('Visit on github: leonardinobre')

sleep(5)

