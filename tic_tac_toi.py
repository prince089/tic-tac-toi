#hello i am prince from india.
#this code is for simple tic-tak-toi using python.
#i hope i help you with this code have a good day dear!!!!!


raw = [[1,2,3], [4,5,6],[7,8,9]] #this is simple 2d array for our base



def play(player_1,player_2):
    #heare we simple disply which player have which symbole
    print("player_1 have 'X' sign")
    print("player_2 have 'O' sign")

    #this switch_player is for switching both player's turn
    switch_player = 1

    while (1):


#heare this switch_play how work its simple odd or even method

        if (switch_player % 2):
            print("player 1's turn you have to put 'X' :")
            place_mark(player_1)
        else:
            place_mark(player_2)
            print("player 2's turn you have to put 'o' :")
        switch_player += 1












def place_mark(player):
    while(1):
#heare we display our current bord it mean with symbol
        print(f"{raw[0][0]} | {raw[0][1]} | {raw[0][2]}")
        print("---------")
        print(f"{raw[1][0]} | {raw[1][1]} | {raw[1][2]}")
        print("---------")
        print(f"{raw[2][0]} | {raw[2][1]} | {raw[2][2]}")
        print("---------")
#heare we take input from use and check whether this place is avalibel or not if avaliable then player can play his/her move and we also check condition of bord for someone winn or not if win then we exit .
        ch = int(input(f"enter your choice  {player}"))
        if (ch == 1):
            if raw[0][0] == 1:
                raw[0][0] = player
                if ((raw[0][0] == raw[0][1] == raw[0][2]) or (raw[0][0] == raw[1][1] == raw[2][2]) or (raw[0][0] == raw[1][0] == raw[2][0])):
                    print(f"congroutulatio team ''' {player} ''' just won !!")
                    exit()

                break

            else:
                print("invealid position")

        if (ch == 2):
            if raw[0][1] == 2:
                raw[0][1] = player
                if ((raw[0][0] == raw[0][1] == raw[0][2]) or (raw[0][1] == raw[1][1] == raw[2][1])):
                    print(f"congroutulatio team ''' {player} ''' just won !!")
                    exit()
                break

            else:
                print("invealid position")

        if (ch == 3):
            if raw[0][2] == 3:
                raw[0][2] = player
                if ((raw[0][0] == raw[0][1] == raw[0][2]) or (raw[0][0] == raw[1][1] == raw[2][2]) or (raw[0][0] == raw[1][0] == raw[2][0])):
                    print(f"congroutulatio team ''' {player} ''' just won !!")
                    exit()
                break

            else:
                print("invealid position")

        if (ch == 4):
            if raw[1][0] == 4:
                raw[1][0] = player
                if ((raw[0][0] == raw[1][0] == raw[2][0]) or (raw[1][0] == raw[1][1] == raw[1][2])):
                    print(f"congroutulatio team ''' {player} ''' just won !!")
                    exit()
                break

            else:
                print("invealid position")

        if (ch == 5):
            if raw[1][1] == 5:
                raw[1][1] = player
                if ((raw[0][0] == raw[0][1] == raw[0][2]) or (raw[0][0] == raw[1][1] == raw[2][2]) or (raw[0][0] == raw[1][0] == raw[2][0]) or (raw[0][1] == raw[1][1] == raw[2][1] ) or (raw[1][0] == raw[1][1] == raw[1][2])):
                    print(f"congroutulatio team ''' {player} ''' just won !!")
                    exit()
                break

            else:
                print("invealid position")

        if (ch == 6):
            if raw[1][2] == 6:
                raw[1][2] = player
                if ((raw[0][2] == raw[1][2] == raw[2][2]) or (raw[1][0] == raw[1][1] == raw[1][2])):
                    print(f"congroutulatio team ''' {player} ''' just won !!")
                    exit()
                break

            else:
                print("invealid position")

        if (ch == 7):
            if raw[2][0] == 7:
                raw[2][0] = player
                if ((raw[0][0] == raw[0][1] == raw[0][2]) or (raw[0][0] == raw[1][1] == raw[2][2]) or (raw[0][0] == raw[1][0] == raw[2][0])):
                    print(f"congroutulatio team ''' {player} ''' just won !!")
                    exit()
                break

            else:
                print("invealid position")


        if (ch == 8):
            if raw[2][1] == 8:
                raw[2][1] = player
                if ((raw[0][1] == raw[1][1] == raw[2][1]) or (raw[2][0] == raw[2][1] == raw[2][2])):
                    print(f"congroutulatio team ''' {player} ''' just won !!")
                    exit()
                break

            else:
                print("invealid position")

        if (ch == 9):
            if raw[2][2] == 9:
                raw[2][2] = player
                if ((raw[0][0] == raw[0][1] == raw[0][2]) or (raw[0][0] == raw[1][1] == raw[2][2]) or (raw[0][0] == raw[1][0] == raw[2][0])):
                    print(f"congroutulatio team ''' {player} ''' just won !!")
                    exit()
                break

            else:
                print("invealid position")
                continue
        if(raw[0][0] != 1 and raw[0][1] != 2 and raw[0][2] != 3 and raw[1][0] != 4 and raw[1][1] != 5 and raw[1][2] != 6 and  raw[2][0] != 7 and raw[2][1] != 8 and raw[2][2] != 9):
            print("i am really sorry noone can win this game ")
            exit()
        else:
            print("this choice is out of world you fool or you trying to overwrite someone's move you cheater")



#heare we declare two varible with his/her symbole to play
player_1 = "X"
player_2 = "o"

#we start playing game and just call function call with both player
play(player_1,player_2)


