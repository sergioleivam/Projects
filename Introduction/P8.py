def game_board(player=0, row=0, column=0, just_display=False):
    print("  a  b  c")
    if not just_display:
        #It works when just_display is false
        game[row][column] = player
        # Therefore, if just_display = True we do not make any changes
    game[row][column] = player
    for count_en, row in enumerate(game):
        print(count_en,row)

# Some tests 
game_board(just_display=True)
game_board(player=1, row=2, column=1)
