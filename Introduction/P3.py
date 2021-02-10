###############################
########   Part 3    ##########
###############################



# We want to program tic-tac-toe
# Using lists

#Firts try:
game = (0,0,0,
        0,0,0,
        0,0,0,)

print (game)
# it print: (0,0,0,0,0,0,0,0,0) i.e. a "flat tuple", which cannot modify
# So, we should use list by changing the ()-parenthesis to []-parenthesis:

game = [0,0,0,
        0,0,0,
        0,0,0,]

# Print type
print(type(game))

# We still have a "flat list", but we would like people to undestand the game
# in order to do so, we can make a list of lists, where we enclose three 0's at a time with []

game = [[0,0,0],
        [0,0,0],
        [0,0,0],]

print(game)
#But it still not printed as we would like. Here we can use what we have learn in the last part: iteration.

for row in game:
    #we read each list in the list game
    print(row)

# In order to make it "user-friendly", we should include something to make easy to indicate 
#  where the user wants to make a move. We are going to do it in the next part.


