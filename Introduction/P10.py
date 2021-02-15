###############################
########   Part 10    ##########
###############################

##### Winner?
#########################

# Suppose a game in this way
game = [[1,1,1],
        [0,2,0],
        [2,2,0],]

# Ways to win:
# 1) Horizontally
# 2) Vertical
# 3) Diagonal

#1. Horizontally
# A naive way would be compare the first element of each column of the row with the rest of the row, 
# but that can get very messy very quickly
# So, another way is:

def win(current_game):
    for row in game:
        print(row)
        col1 = row[0]
        col2 = row[1]
        col3 = row[2]
        
        if col1 == col2 == col3:
            print("winner !!!")

win(game)