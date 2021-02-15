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

check = []     # list to check

# for row in game:
#     check.append(row[0]) # We add the element of the row to the check-list.

# # Re using the structure of the horizontal win:

# if check.count(check[0]) == len(check) and check[0] != 0:
#     print("Winner!")

# Lets check if we dont win
game = [[2,0,1],
        [0,0,0],
        [2,2,0],]

check = []     # list to check

for row in game:
    check.append(row[0]) # We add the element of the row to the check-list.

# Re using the structure of the horizontal win:

if check.count(check[0]) == len(check) and check[0] != 0:
    print("Winner!")
