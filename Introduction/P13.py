###############################
########   Part 13    ##########
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