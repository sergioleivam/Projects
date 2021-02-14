###############################
########   Part 9    ##########
###############################

game = [[0,0,0],
        [0,0,0],
        [0,0,0],]

def game_board(game_map,player=0, row=0, column=0, just_display=False):
    print("  a  b  c")
    if not just_display:
        game_map[row][column] = player
    for count_en, row in enumerate(game_map):
        print(count_en,row)

    return game_map

# We now need to assign the variable that we want to modify, equal to the function
game = game_board(game, just_display=True)
game = game_board(game, player=1,row=2,column=1)
