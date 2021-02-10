###############################
########   Part 7    ##########
###############################

game = [[0,0,0],
        [0,0,0],
        [0,0,0],]


def game_board():
    print("  a  b  c")
    for count_en, row in enumerate(game):
        print(count_en,row)
    

game_board()

game[0][1] = 1

game_board()
