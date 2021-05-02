coord_list = ["0 0", "0 1", "0 2", "0 3", "1 0", "1 1", "1 2", "1 3", "2 0", "2 1", "2 2", "2 3", "3 0", "3 1", "3 2", "3 3"]
printed_list = ["_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_"]
turn = 1
def player_turn(player):
    print(f"Player {player}'s turn!")
    return input("New coordinates: ")
def coord_change(players_turn, coords):
    if players_turn == 1:
        printed_list[coord_list.index(coords)] = "O"
    if players_turn == 2:
        printed_list[coord_list.index(coords)] = "X"
def print_board():
    for i in range(len(printed_list)):
        print(printed_list[i], end=" ")
        if (i + 1) % 4 == 0:
            print(end="\n")
def prevent_overlap(coordi):
    if printed_list[coord_list.index(coordi)] == "O" or printed_list[coord_list.index(coordi)] == "X":
        print("These coordinates are invalid.")
        exit()
def check_win(player):
    if player == 1:
        game_unit = "O"
    else:
        game_unit = "X"

    if printed_list[0] == printed_list[1] == printed_list[2] ==printed_list[3]== game_unit or printed_list[4] == printed_list[5] == printed_list[6] == printed_list[7] == game_unit or printed_list[8] == printed_list[9] == printed_list[10] == printed_list[11]== game_unit or printed_list[12] == printed_list[13] == printed_list[14] ==printed_list[15]== game_unit or printed_list[0] == printed_list[4] == printed_list[8] ==printed_list[12]== game_unit or printed_list[1] == printed_list[5] == printed_list[9] == printed_list[13]== game_unit or printed_list[2] == printed_list[6] == printed_list[10] == printed_list[14] == game_unit or printed_list[3] == printed_list[7] == printed_list[11] == printed_list[15] == game_unit or printed_list[0] == printed_list[5] == printed_list[10] == printed_list[15] == game_unit or printed_list[12] == printed_list[9] == printed_list[6] == printed_list[3] == game_unit:
        print(f"Player {player} win!")
        exit()
print("Tic Tac Toe game starts!")
print("------------------------")
while True:
    coord = player_turn(turn)
    prevent_overlap(coord)
    coord_change(turn, coord)
    print_board()
    check_win(turn)
    if turn == 1:
        turn = 2
        continue
    if turn == 2:
        turn = 1
