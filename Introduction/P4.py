###############################
########   Part 4    ##########
###############################


# We resume at:

game = [[0,0,0],
        [0,0,0],
        [0,0,0],]

for row in game:
    #we read each list in the list game
    print(row)

# Print some numbers over the top, with extra spaces so they align with the columns

print("  0  1  2")
for row in game:
    #we read each list in the list game
    print(row)

#To add numbers in a column to the left of the game set, we add a new variable that can count in which row we are:

print("  0  1  2")
count = 0

for row in game:
    print(count,row)
    #After the print we need to add 1 to the counter so in the next row it has another value
    # Here we have 2 options:
    # count = count+1
    count += 1

# Although this is not the "best" way to do it, we can use a Built-in functions of python
# we know are going to use: enumerate
# which as it iterate over something, it returns both the index value and the value

print("  0  1  2")
for count_en, row in enumerate(game):
    # It is not good to use a pre-existing variable as the variable of the for to iterate, so we use count_en for this case.
    print(count_en,row)

# We can furthermore print element by element in each row of the game, we only have to introduce another for

for count_en, row in enumerate(game):
    for item in row:
        print(item)

# A more clear way to print the game would be using both lettlers and numbers for column and rows

print("  a  b  c")
for count_en, row in enumerate(game):
    print(count_en,row)



