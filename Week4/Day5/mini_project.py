def display_board(mov):
    board = '''
    TIC TAC TOE
    ***************
    *  {1_1} | {1_2} | {1_3}  *
    *  --|---|--- *
    *  {2_1} | {2_2} | {2_3}  *
    *  --|---|--- *
    *  {3_1} | {3_2} | {3_3}  *
    ***************
    '''.format(**mov)

    print(board)

row_x = ""
row_o = ""
column_x = ""
column_o = ""


# #to check whose turn it is: player_x and o due if turn divisible by 2 & remainder = 0 then it's x turn
def player_input(player, moves):

    print("Player", player, " turn:")
    row = input(str("Enter row: "))
    column = input(str("Enter column: "))
    selection = row + "_" + column
    moves[selection] = player
    # return selection, player
         

# def check_win(player, moves):
#     list_moves = []
    

    # for key, value in moves.items():
    #     # if list_moves[2][0] == "1":
    #     #     print("yo")
    #     if value == player:
    #         list_moves.append(key)
    #         # if list_moves[0][0].startswith("1"):
    #         #         print("yo")
    
    # for value in list_moves:
    #     if list_moves[0][0] == list_moves[1][0] == list_moves[2][0]:
    #         print("game over1!", player, "won")
    #         print(list_moves[0][0])
    #         break
    #     elif list_moves[0][2] == list_moves[1][2] == list_moves[2][2]:
    #         print("game over2!", player, "won")
    #         break
    
    #     # elif list_moves[0][3] == list_moves[1][3] == list_moves[2][3]:
    #     #     print("game over!", player, "won")
    #     #     break
        
    # print(list_moves)
    # return list_moves



#1_1
# list.moves[0][2]


def play():
    print("Welcome to TIC TAC TOE!")
  
    moves = {
        "1_1" : " ",
        "1_2" : " ",
        "1_3" : " ",
        "2_1" : " ",
        "2_2" : " ",
        "2_3" : " ",
        "3_1" : " ",
        "3_2" : " ",
        "3_3" : " ",
    }

    display_board(moves)

    for round in range(1,10):
        if round%2 == 0:
            player = "X"
        
        else:
            player = "O"
        player_input(player, moves)
        display_board(moves)

        if round >= 5 and round <= 10:
            list_moves = []
    
            for key, value in moves.items():
                # if list_moves[2][0] == "1":
                #     print("yo")
                if value == player:
                    list_moves.append(key)
                    # if list_moves[0][0].startswith("1"):
                    #         print("yo")
            
            for value in list_moves:
                if list_moves[0][0] == list_moves[1][0] == list_moves[2][0]:
                    print("game over1!", player, "won")
                    print(list_moves[0][1])
                    break
                elif list_moves[0][2] == list_moves[1][2] == list_moves[2][2]:
                    print("game over2!", player, "won")
                    break
                #1_1 2_2 3_3
                elif "1_1" and "2_2" and "3_3" in list_moves:
                    print("game over3!", player, "won")
                    break
                elif "1_3" and "2_2" and "3_1" in list_moves:
                    print("game over4!", player, "won")
                    break
                # return list_moves

                else:
                    round += 1
                    continue
            

            

play()

