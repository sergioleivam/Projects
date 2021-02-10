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