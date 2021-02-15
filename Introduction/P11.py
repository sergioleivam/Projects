###############################
########   Part 10    ##########
###############################

##### Winner?
#########################

# Suppose a game in this way
game = [[2,0,1],
        [2,0,0],
        [2,2,0],]

# Ways to win:
# 1) Horizontally
# 2) Vertical
# 3) Diagonal

# 2) Vertical 

# To check this kind of win, we need to check the same index in every row to be the same. Like:

for row in game:
    print(row[0])