###############################
########   Part 14    #########
###############################
import itertools

play = False     # So we dont init a game
players = [1, 2]

while play:  
    game = [[0,0,0],  
            [0,0,0],
            [0,0,0]]

    game_won = False
    game = game_board(game, just_display=True)
    player_choice = itertools.cycle(players)  
    while not game_won:
        current_player = next(player_choice)
        print(f"Current player: {current_player}")
        column_choice = int(input("What column do you want to play? (0, 1, 2):  "))  
        row_choice = int(input("What row do you want to play? (0, 1, 2):  ")) 

        # Make the move
        game = game_board(game, current_player, column_choice, row_choice)


# We have to fixed some problems:

# 1) Not alow to play over an existing move

def game_board(game_map,player=0, row=0, column=0, just_display=False):
    try:
        if game_map[row][column] != 0:
            print("This position is occupado! Choose another")
            return game_map, False
        print("  a  b  c")
        if not just_display:
            game_map[row][column] = player
        for count_en, row in enumerate(game_map):
            print(count_en,row)
        return game_map, True

    except IndexError as e:
        print("Error: make sure you input row/column as 0 1 or 2",e)
        return game_map, False
    except Exception as e:
        print("Something went very wrong! ",e)
        return game_map, False

# With the False returned when it has been an error or a restricted move, the player
# does not lose the turn.


play = False     
players = [1, 2]

while play:  
    game = [[0,0,0],  
            [0,0,0],
            [0,0,0]]

    game_won = False
    game, _ = game_board(game, just_display=True)  # When we don't care about a variable, we use "_"
    player_choice = itertools.cycle(players)  
    while not game_won:
        current_player = next(player_choice)
        print(f"Current player: {current_player}")
        played = False                              # So we can ask if the play is well defined

        while not played:
            column_choice = int(input("What column do you want to play? (0, 1, 2):  "))  
            row_choice = int(input("What row do you want to play? (0, 1, 2):  ")) 
            game, played = game_board(game, current_player, column_choice, row_choice)
            
# We have a problem that, after a single bad move, the game is now equal to False, which is not what we want
# To fixed it, we have change what game give as return the
# Now, it return (game, True/False)

# 2) Compactify the win and applying to the game

# We can see that the function win has the same lines repited, so we can define a function that do that.

def win(current_game):

    def all_same(l):
        if l.count(l[0]) == len(l) and l[0] != 0:
            return True
        else:
            return False

    # Horizontal
    for row in game:
        if all_same(row): 
            print(f"Player {row[0]} is the winner horizontally") 
            return True

    # Vertical
    for col in range(len(game)):
        check = []
        for row in game:
            check.append(row[col])
        
        if all_same(check):
            print(f"Player {check[0]} is the winner Verticaly")
            return True

    # Diagonal
    diags = []
    for col, row in enumerate(reversed(range(len(game)))):
            diags.append(game[row][col])
    if all_same(diags):
        print(f"Player {diags[0]} is the winner Diagonaly ( / )")
        return True
    diags = []
    for ix in range(len(game)):
            diags.append(game[ix][ix])
    
    if all_same(diags):
        print(f"Player {diags[0]} is the winner Diagonaly ( \\ )")
        return True
    
    return False

# Add the above changes to the game

play = False     
players = [1, 2]

while play:  
    game = [[0,0,0],  
            [0,0,0],
            [0,0,0]]

    game_won = False
    game, _ = game_board(game, just_display=True)  # When we don't care about a variable, we use "_"
    player_choice = itertools.cycle(players)  
    while not game_won:
        current_player = next(player_choice)
        print(f"Current player: {current_player}")
        played = False                              # So we can ask if the play is well defined

        while not played:
            column_choice = int(input("What column do you want to play? (0, 1, 2):  "))  
            row_choice = int(input("What row do you want to play? (0, 1, 2):  ")) 
            game, played = game_board(game, current_player, column_choice, row_choice)
        
        if win(game):
            game_won = True
            again = input("The game is over, would you like to play again? (y/n):  ")
            if again.lower() == "y":
                # If the user use different case of letters, we can use .lower or .upper to modify all
                print("restarting ")
            elif again.lower() == "n":
                # If the first is if work and we define this one as if, it will run it anyways so it is better to use elif that combine an else with an if
                print("Byeeee ")
                play = False
            else:                     # Bad user
                print("Not a valid answer, so ... c u l8r aligator")

# Now we can finised the game

# 3) Lack of dynamics of the string "   0  1  2"

# To make dynamics we can separate it into the main values 
# game_size = 3
# print("   0  1  2")
# s = " "  # one space, the initial value of the string
# for i in range(game_size):
#     s += "  "+str(i)

# print(s)

# Another option is using .join()

# s = "   "+ "  ".join([str(i) for i in range(game_size)])

# print(s)

def game_board(game_map,player=0, row=0, column=0, just_display=False):
    try:
        if game_map[row][column] != 0:
            print("This position is occupado! Choose another")
            return game_map, False
        print("   "+ "  ".join([str(i) for i in range(len(game_map))]))
        if not just_display:
            game_map[row][column] = player
        for count_en, row in enumerate(game_map):
            print(count_en,row)
        return game_map, True

    except IndexError as e:
        print("Error: make sure you input row/column as 0 1 or 2",e)
        return game_map, False
    except Exception as e:
        print("Something went very wrong! ",e)
        return game_map, False

play = False     
players = [1, 2]

while play:  
    game = [[0,0,0],  
            [0,0,0],
            [0,0,0]]

    game_won = False
    game, _ = game_board(game, just_display=True)  # When we don't care about a variable, we use "_"
    player_choice = itertools.cycle(players)  
    while not game_won:
        current_player = next(player_choice)
        print(f"Current player: {current_player}")
        played = False                              # So we can ask if the play is well defined

        while not played:
            column_choice = int(input("What column do you want to play? (0, 1, 2):  "))  
            row_choice = int(input("What row do you want to play? (0, 1, 2):  ")) 
            game, played = game_board(game, current_player, column_choice, row_choice)
        
        if win(game):
            game_won = True
            again = input("The game is over, would you like to play again? (y/n):  ")
            if again.lower() == "y":
                # If the user use different case of letters, we can use .lower or .upper to modify all
                print("restarting ")
            elif again.lower() == "n":
                # If the first is if work and we define this one as if, it will run it anyways so it is better to use elif that combine an else with an if
                print("Byeeee ")
                play = False
            else:                     # Bad user
                print("Not a valid answer, so ... c u l8r aligator")

# A very useful third party library is numpy 
# we can install it by: py -3.7 -m pip install numpy
# in the terminal
# then in our code we imported it as:
# import numpy as np
# And use it like:
# np.zeros(5)
# np.zeros((3,3))

# The last part is:  dictionaries

#  Dictionaries is just a way to have keys and values like

dictionaries = {"key1":15, "key2":32}

print(dictionaries["key1"])

# Add another key
dictionaries["hithere"] = 92

# Ask the whole dictionary
print(dictionaries)