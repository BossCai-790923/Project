'''
Requirement:
Implement Game: tic-tac-toe
Key Logic:
If we analysis the process of the game, we know the game is composed of the following steps.
'''
'''
Step 1) Prepare data.
        Create an empty chess board.
        tic-tac-toe game chess board is composed of 9 spaces - 3 * 3
        So we can use a nested list to represent the chess board.
'''
chess_board = [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]
'''
Step 2) Print chess board to the console.
        I define a function to print the chessboard nicely.
        And this function will be called many times.
'''
def print_chessboard(chess_bard):
    '''
    This function prints the chess board
    :param chess_bard:
    :return: nothing
    '''
    for row in chess_bard:
        print(*row)
'''
Step 3) Player places a piece.
        We define a new function. The function will accept 2 parameter - chess_board, piece (being either 'X' or 'O')  
        def place_piece(chess_board, piece):
            pass

And inside the function body, it should do the following steps.
Step 3.1) We ask player to input the coordinates x and y.
       We define a new function, we let the function return a list which contains coordinates x and y
       def get_user_coordinates():
            pass

Step 3.2) We check coordinates x and y, with the below conditions:
       Condition check No.1) x and y value should be in range [0,2].   
       Condition check No.2) chess_board[x][y] should be '_', meaning it is not taken by Player 1 or 2.
       If any of the condition fail, then we need to repeat step 3.1) and step 3.2) 
       We define a new function, we let the function return a bool value; 
       True -> valid coordinates;
       False -> invalid coordinates;
       def check_coordinates(coordinates):
           pass

So, step 3.1) and step 3.2) should be put in a loop.

Step 3.3) update chess_board, very simple
    chess_board[x][y] = piece

Step 3.4) print chess_board, very simple, we call function: print_chessboard(chess_board)           
Step 3.5) check win.
    For the new coordinates where the player has placed the piece on, check whether he wins or not.
    if he wins, program exit.
    if he doesn't win: does nothing. 
    We define a new function:
    def check_win(chess_board, coordinates):
        pass              
'''
def get_user_coordinates():
    '''
    We ask user to input the coordinates.
    :return: a list which contains 2 int in it, being x and y.
    '''
    input_value = input("New coordinates: ")
    x_y_list = input_value.split(' ')  # if user input '1 2', x_y_list will become list ['1', '2']
    x = int(x_y_list[0])
    y = int(x_y_list[1])
    return [x, y]
def check_coordinates(chess_board, coordinates):
    '''
    check whether the coordinates is valid for the chess_board or not
    :param chess_board:
    :param coordinates: is a list, which contains int x and y
    :return: True if both x and y are within range [0,2] and chess_board[x][y] has not been taken by any player.
    '''
    x = coordinates[0]
    y = coordinates[1]
    if x < 0 or x > 2:
        print(f"Coordinates x is wrong {x}. Valid value is in range[0, 2]. Please try again.")
        return False
    if y < 0 or y > 2:
        print(f"Coordinates y is wrong {y}. Valid value is in range[0, 2]. Please try again.")
        return False
    if chess_board[x][y] != '_':
        print(f"chessboard [{x}][{y}] has value {chess_board[x][y]}. Pleass try again.")
        return False
    return True
def check_win(chess_board, coordinates):
    '''
    This function checks whether the coordinates will cause a win in the chessboard.
    If somebody win, the program exit.
    :param chess_board:
    :param coordinates: is list
    :return: Nothing
    '''
    x = coordinates[0]
    y = coordinates[1]
    if chess_board[x][0] == chess_board[x][1] and chess_board[x][0] == chess_board[x][2]:
        print("win!")
        exit()
    if chess_board[0][y] == chess_board[1][y] and chess_board[0][y] == chess_board[2][y]:
        print("win!")
        exit()
    if x == 0 and y == 0 or x == 2 and y == 2 or x == 1 and y == 1:
        if chess_board[0][0] == chess_board[1][1] and chess_board[0][0] == chess_board[2][2]:
            print("win!")
            exit()
    if x == 0 and y == 2 or x == 2 and y == 0 or x == 1 and y == 1:
        if chess_board[2][0] == chess_board[1][1] and chess_board[2][0] == chess_board[0][2]:
            print("win!")
            exit()
def place_piece(chess_board, piece):
    '''
    This function will place a piece in the chessboard
    :param chess_board:
    :param piece: It can be either 'X' or 'O'
    :return: nothing
    '''
    while True:
        coordinates = get_user_coordinates()
        is_valid_coordinates = check_coordinates(chess_board, coordinates)
        if is_valid_coordinates:
            break
    chess_board[coordinates[0]][coordinates[1]] = piece
    print_chessboard(chess_board)
    check_win(chess_board, coordinates)
    print('_' * 20)
welcome_msg = '''Tic Tac Toe Game Starts:
--------------------------------------------
'''
print(welcome_msg)
print_chessboard(chess_board)
player1 = ['PLAYER 1', 'O']
player2 = ['PLAYER 2', 'X']
players = [player1, player2]
for turn in range(9):
    player = players[turn % 2]
    print(f"{player[0]}'s turn:")
    place_piece(chess_board, player[1])
print("Nobody wins！")
