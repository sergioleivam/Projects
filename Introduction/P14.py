###############################
########   Part 14    #########
###############################
import itertools

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
        column_choice = int(input("What column do you want to play? (0, 1, 2):  "))  
        row_choice = int(input("What row do you want to play? (0, 1, 2):  ")) 

        # Make the move
        game = game_board(game, current_player, column_choice, row_choice)


# We have to fixed some problems:
