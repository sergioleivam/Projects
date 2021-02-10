###############################
########   Part 5    ##########
###############################


# First we need to know how to ask an specific value on a list:

l = [1,2,3,4,5]

# Print the whole list
print(l)

# Print the zeroth element of the list
print(l[0])

# Print the elements between the index 1 and 3 of the list
print(l[1:3])

# Print the elements from the third index to the end of the list
print(l[2:])

# Set a new value for the element of the list with index 1:

l[1] = 99
print(l)


# In our game, we have a list of lists so


game = [[0,0,0],
        [0,0,0],
        [0,0,0],]

print("  a  b  c")
for count_en, row in enumerate(game):
    print(count_en,row)

# If we print game[0], we print the first row:

print(game[0])

# To change a single element we can use an identification of the value of
#  game at row 0 and column 1, with game[0][1]

game[0][1] = 1

print("  a  b  c")
for count_en, row in enumerate(game):
    print(count_en,row)

# Now we can repeat the above lines to apply the users moves, but changes are, we would make a mistake in that
# process, and it would make the code hard or tedious to read. 
# At this point it is useful to define a function that do those lines.