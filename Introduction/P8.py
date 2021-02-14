###############################
########   Part 7    ##########
###############################

# Lets talk about mutability
# It can be very tricky when we have a bigger code and we are re-reading it.
# It we want modify a value outside of a function. If we have a lists of list, we can just 
#  modify an individual element as we have been doing but it will not always work.

# Some examples to show a 'superior' method 

# game = [[0,0,0],
#         [0,0,0],
#         [0,0,0],]

# def game_board(player=0, row=0, column=0, just_display=False):
#     print("  a  b  c")
#     if not just_display:
#         game[row][column] = player
#     for count_en, row in enumerate(game):
#         print(count_en,row)

# game_board()

# # Now we want that function to return the game board, so:

# print(game)
# game_board(player=1,row=1,column=1)
# print(game)


# # Change the initial game and the function to

# game = "I want to play a game"
# # We can check the id of a certain variable with the built-in function: id()
# print(id(game))

# def game_board(player=0, row=0, column=0, just_display=False):
#     game = "A game"
#     # This modification wont work, because it change a "local" variable inside the function
#     # However, if we print game inside the function as:
#     print(game)
#     # We see that it "work"
#     print(id(game))

# print(game)
# game_board()
# print(game)
# print(id(game))

# A string is unmutable, so we cannot change it

# If we go back to test with list but inside the function we set a string

game = [1,2,3]
print(id(game))

def game_board(player=0, row=0, column=0, just_display=False):
    game = "A game"
    print(id(game))
    print(game)

game_board()
print(game)
print(id(game))

# In this case, we do not change the original game and end up printing [1,2,3]

# If we do the same, only this time we set an specifical value of game as:

game = [1,2,3]
print(id(game))

def game_board(player=0, row=0, column=0, just_display=False):
    game[1] = 99
    print(id(game))
    print(game)

game_board()
print(game)
print(id(game))

# We can see that the id's when we mixed strings and lists, are different
# but if we indicate a direct modification of an element it does not change.

# In the end, if we try to change the whole variable, it won't work.

# The last part here, is that if we go back to

game = "I want to play a game"
print(id(game))

def game_board(player=0, row=0, column=0, just_display=False):
    global game
    # Set the variable "game" to be a global accesible and manipulable, i.e. global value
    game= "A game"
    print(id(game))
    print(game)

game_board()
print(game)