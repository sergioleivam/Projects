###############################
########   Part 7    ##########
###############################

# Examples of functions with parameters

def addition(x,y):
    return x+y

# We have to be careful because python work without variable previously identify. Python works with dinamics variables
#  this is very important in cython that kind of mix both python and C 

game = [[0,0,0],
        [0,0,0],
        [0,0,0],]

# We are going to modify our earlier function game_board to include parameters:

def game_board(player, row, column):
    print("  a  b  c")
    for count_en, row in enumerate(game):
        print(count_en,row)
    

#Even though those parameters are for now useless, the code will fail because it need those values to evaluate the function.
#game_board()

#We can set default values for each parameter so if we call the function without those parameters the function will know what to do.

def game_board(player=0, row=0, column=0):
    print("  a  b  c")
    #Set the move
    game[row][column] = player
    for count_en, row in enumerate(game):
        print(count_en,row)

game_board()
# For readability
game_board(player=1,row=2,3)
game_board(player=1,row=2,column=3)

# Add some conditions to work
def game_board(player=0, row=0, column=0):
    print("  a  b  c")
    if player != 0:
        # != means not equal
        game[row][column] = player
    game[row][column] = player
    for count_en, row in enumerate(game):
        print(count_en,row)

# Add a flag to the parameters

def game_board(player=0, row=0, column=0, just_display=False):
    print("  a  b  c")
    if not just_display:
        #It works when just_display is false
        game[row][column] = player
        # Therefore, if just_display = True we do not make any changes
    game[row][column] = player
    for count_en, row in enumerate(game):
        print(count_en,row)

# Some tests 
game_board(just_display=True)
game_board(player=1, row=2, column=1)