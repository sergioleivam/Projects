###############################
########   Part 7    ##########
###############################

# Lets talk about mutability
# It can be very tricky when we have a bigger code and we are re-reading it.
# It we want modify a value outside of a function. If we have a lists of list, we can just 
#  modify an individual element as we have been doing but it will not always work.

# Some examples to show a 'superior' method 

game = [[0,0,0],
        [0,0,0],
        [0,0,0],]

def game_board(player=0, row=0, column=0, just_display=False):
    print("  a  b  c")
    if not just_display:
        game[row][column] = player
    for count_en, row in enumerate(game):
        print(count_en,row)

game_board()