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

#win(game)

# Problems :
# 1) What happend if we need to change the size of the game to, for example, 4x4
#     or dynamics
#       Sol: We can have many codes, but it is a very very bad idea overall with time. 

# First (not good) solution:

def win(current_game):
    for row in game:
        print(row)
        all_match = True             # Create a flag
        for item in row:
            if item != row[0]:
                all_match = False    # In the video, at first, they use == so it is comparing and not changing the value 
        if all_match:
            print("Winner !!!")

#win(game)

# Too long for a simple task. A little secret to programmer is to use google to our advantage, we can look out 
#  "check if all element in a list python", for example. 

# The solution we can find is using count() or in this case .count()

def win(current_game):
    for row in game:      # I think it should be current_game but I will check it later
        print(row)
        if row.count(row[0]) == len(row): # If the times that the first element is repeated is equal 
        #                                   to the length that means they are all the same value
            print("Winner!")
win(game)