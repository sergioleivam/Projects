###############################
########   Part 12    ##########
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

# 3) Diagonal 

# There are two ways we can win diagonally, and we want to keep it scaleable

game = [[2,0,1],
        [2,2,0],
        [2,2,2],]

# First way, the index has to increase at the same time, [0,0], [0+1,0+1], [1+1,1+1]
# Second way, one index increase and the other decrease by the same amount, [2,0], [2-1,0+1], [1-1,1+1]

# Lets check, hard coding it

if game[0][0] == game[1][1] == game[2][2]:
        print("Winner")
if game[2][0] == game[1][1] == game[0][2]:
        print("Winne")