###############################
########   Part 6    ##########
###############################

game = [[0,0,0],
        [0,0,0],
        [0,0,0],]

print("  a  b  c")
for count_en, row in enumerate(game):
    print(count_en,row)

game[0][1] = 1

print("  a  b  c")
for count_en, row in enumerate(game):
    print(count_en,row)

# First we need to identify why we need it
# For example, if we what to change from "  a  b  c" to "  0  1  2"
#   we can make a function that take that information and only repeated overa and over.

# Another important part when we create a new function, is the name
#  those usually are low-case letters and the name should tell what they do.
# For example, if a function make a sum of values, then the name should be sum. So when we read
# the code, we intantly know that that function make sums.

game = [[0,0,0],
        [0,0,0],
        [0,0,0],]

def game_board():
    # Inside the parenthesis, we list the parameters that would need our new function
    print("  a  b  c")
    for count_en, row in enumerate(game):
        print(count_en,row)
    
    #It is important to note the indentation above

# Now we can make the same game with:

game_board()

game[0][1] = 1

game_board()

# If we forgot to put the parenthesis i.e. game_board instead of game_board(), the function won't do anything.

# We also can create a the same function with another name as

x = game_board   # Without parenthesis