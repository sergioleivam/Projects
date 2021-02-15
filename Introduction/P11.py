###############################
########   Part 11    ##########
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

check = []     # list to check

# for row in game:
#     check.append(row[0]) # We add the element of the row to the check-list.

# # Re using the structure of the horizontal win:

# if check.count(check[0]) == len(check) and check[0] != 0:
#     print("Winner!")

# Lets check if we dont win
# game = [[2,0,1],
#         [0,0,0],
#         [2,2,0],]

# check = []     # list to check

# for row in game:
#     check.append(row[0]) # We add the element of the row to the check-list.

# # Re using the structure of the horizontal win:

# if check.count(check[0]) == len(check) and check[0] != 0:
#     print("Winner!")



# This only works if we win with the zeroth column. To keep it as dynamic as possible:

# game = [[2,0,1],
#         [1,0,1],
#         [2,2,1],]

# columns = [0,1,2]      # Here we have to change it if we change the dimensions of the game

# for col in columns:
#     check = []

#     for row in game:
#         check.append(row[col]) 

#     if check.count(check[col]) == len(check) and check[col] != 0:
#         print("Winner!")

# We can use len(game) that would be 3 for our case. So:

game = [[2,0,1],
        [1,0,1],
        [2,2,1],]

for col in range(len(game)):    # range is a built-in function (although it is not a function
    check = []                  #, very useful, that make a list of the a given size and step.
    for row in game:
        check.append(row[col])
    
    if check.count(check[col]) == len(check) and check[col] != 0:
        print("Winner!")