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
            return False
        print("  a  b  c")
        if not just_display:
            game_map[row][column] = player
        for count_en, row in enumerate(game_map):
            print(count_en,row)
        return game_map

    except IndexError as e:
        print("Error: make sure you input row/column as 0 1 or 2",e)
        return False
    except Exception as e:
        print("Something went very wrong! ",e)
        return False

# With the False returned when it has been an error or a restricted move, the player
# does not lose the turn.


play = True     
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
        played = False                              # So we can ask if the play is well defined

        while not played:
            column_choice = int(input("What column do you want to play? (0, 1, 2):  "))  
            row_choice = int(input("What row do you want to play? (0, 1, 2):  ")) 
            game = game_board(game, current_player, column_choice, row_choice)
            if game:
                played = True
