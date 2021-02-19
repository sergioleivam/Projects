###############################
########   Part 13    #########
###############################

game = [[2,0,1],
        [1,0,1],
        [2,2,1],]

# Lets bring all the ways to win:


# Horizontal

def win(current_game):
    for row in game:
        if row.count(row[0]) == len(row) and row[0] != 0: 
            print(f"Player {row[0]} is the winner horizontally") # the f before the string, makes an "f-string" that allow us to input variables

    # Vertical

    for col in range(len(game)):
        check = []
        for row in game:
            check.append(row[col])
        
        if check.count(check[col]) == len(check) and check[col] != 0:
            print(f"Player {check[0]} is the winner Verticaly")

    # Diagonal

    diags = []

    for col, row in enumerate(reversed(range(len(game)))):
            diags.append(game[row][col])

    if diags.count(diags[col]) == len(diags) and diags[0] != 0:
        print(f"Player {diags[0]} is the winner Diagonaly ( / )")
    
    diags = []

    for ix in range(len(game)):
            diags.append(game[ix][ix])
    
    if diags.count(diags[col]) == len(diags) and diags[0] != 0:
        print(f"Player {diags[0]} is the winner Diagonaly ( \\ )") # If we want to see a "\" we need to cancel its value or function by \\



# Bring back board_game

def game_board(game_map,player=0, row=0, column=0, just_display=False):
    try:
        print("  a  b  c")
        if not just_display:
            game_map[row][column] = player
        for count_en, row in enumerate(game_map):
            print(count_en,row)
        return game_map

    except IndexError as e:
        print("Error: make sure you input row/column as 0 1 or 2",e)
    except Exception as e:
        print("Something went very wrong! ",e)

# game = game_board(game, just_display=True)
# game = game_board(game_board, player=1,row=3,column=1)



# Let's init the game

play = True
players = [1, 2]

while play:  # play = True, we are playing, play = False we have finished the game
    game = [[0,0,0],  # When we start the game
            [0,0,0],
            [0,0,0]]

    game_won = False
    game = game_board(game, just_display=True)
    while not game_won:
        current_player = 1    # We have to come back here to define dynamically which player is playing
        
        column_choice = input("What column do you want to play? (0, 1, 2)")  # With input we ask the players
        row_choice = input("What row do you want to play? (0, 1, 2)")  # With input we ask the players

        # Make the move
        game = game_board(game, current_player, column_choice, row_choice)
        










# Test a horizontally win:

game = [[2,2,2],
        [1,0,1],
        [2,2,1],]

win(game)

# Test a Vertical win:

game = [[2,1,2],
        [2,0,1],
        [2,2,1],]

win(game)

# Test a (\)-Diagonal  win:

game = [[2,1,2],
        [1,2,1],
        [1,1,2],]

win(game)

# Test a (/)-Diagonal  win:

game = [[2,1,2],
        [1,2,1],
        [2,1,1],]

win(game)