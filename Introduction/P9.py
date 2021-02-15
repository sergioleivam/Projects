###############################
########   Part 9    ##########
###############################

##### Error Handling
#########################

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

# This time, we will study what happen when a possible user make "bad use" of our app or code

# For example, if the user try to change the value of the game in row: 3
#  in this case, the error will be IndexError: list index out of range. Meaning
#  that the value of the index we enter, exceed the width of the list.

# To handle this error, we know that this error may appear for a many reasons
#  we can add the enviroment try: (to test if it is ok and do it) and excent: (something to do if it is not ok)

def game_board(game_map,player=0, row=0, column=0, just_display=False):
    try:
        print("  a  b  c")
        if not just_display:
            game_map[row][column] = player
        for count_en, row in enumerate(game_map):
            print(count_en,row)
        return game_map
    except:
        print("something went wrong !!!")

game = game_board(game, just_display=True)
game = game_board(game, player=1,row=3,column=1)


# If you don't know what the error means, you always can look it up in google!.
