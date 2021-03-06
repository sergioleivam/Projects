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
# game = game_board(game, just_display=True)
# game = game_board(game, player=1,row=2,column=1)

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

# game = game_board(game, just_display=True)
# game = game_board(game, player=1,row=3,column=1)

# However, with this way, the user does not understand what went wrong so we are not handling the error properly.
# If you don't know what the error means, you always can look it up in google!.

# Another option is to specify the error, and indicate to the user  

print("game is a:  ",type(game))

# Since the last iteration change the variable game to a 'NoneType' we have to create it again
game = [[0,0,0],
        [0,0,0],
        [0,0,0],]

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
        # Here e save the specific error from the terminal.

# game = game_board(game, just_display=True)
# game = game_board(game, player=1,row=3,column=1)

# What happend if the user or programmer input, for example, game_board instead of game as parameter?

# game = game_board(game, just_display=True)
# game = game_board(game_board, player=1,row=3,column=1)

# As a programmer we expect that this kind of error does not happend. Both it still can happend.
# For this kind of situation we can do two things:
# 1) Add another exception from IndexError
# 2) Add a general Exception as

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

game = game_board(game, just_display=True)
game = game_board(game_board, player=1,row=3,column=1)

# When we use try:, there are two other statements that we can use:
# 1) else:
# 2) finally: 
# Although we see them rarely. If you want to use them, look them in google or youtube.

# 3) raise: 
# is also useful to raise an exception of an error