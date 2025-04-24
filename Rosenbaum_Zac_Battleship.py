import sys
import random
import time
from playsound import playsound

board_p1 = [["🌊"] * 5 for i in range(5)]
hid_board_p1 = [["🌊"] * 5 for i in range(5)]
board_p2 = [["🌊"] * 5 for i in range(5)]
hid_board_p2 = [["🌊"] * 5 for i in range(5)]

def show_board(board, player_num):
    print(f"PLAYER {player_num}'s BOARD:")
    print("   1  2  3  4  5")
    row_num = 1
    for row in board:
        print(str(row_num) + " " + ' '.join(row))
        row_num += 1

def player_pieces(board, player, ship_amt):
    ships = 0
    print(f"PLAYER: {player}, PLACE SHIPS")
    while ships < ship_amt:
        try:
            row = int(input("Which row? (1-5): ")) - 1
            col = int(input("Which column? (1-5): ")) - 1
        except ValueError:
            print("NUMBER ONLY")
            continue
        if 0 <= row <= 4 and 0 <= col <= 4 and board[row][col] == "🌊":
            board[row][col] = "🛥️ "
            ships += 1
            show_board(board, player)
        else:
            print("INVALID SPOT, TRY AGAIN")

def comp_pieces(board, ship_amt):
    ships = 0
    while ships < ship_amt:
        row = random.randint(0, 4)
        col = random.randint(0, 4)
        if board[row][col] == "🌊":
            board[row][col] = "🛥️ "
            ships += 1

def guess_ship(board, hid_board, player_num):
    print(f"PLAYER: {player_num} GUESS SPOT")
    while True:
        try:
            row_guess = int(input("Which row? (1-5): ")) - 1
            col_guess = int(input("Which column? (1-5): ")) - 1
        except ValueError:
            print("NUMBER ONLY")
            continue

        if 0 <= row_guess <= 4 and 0 <= col_guess <= 4:
            if hid_board[row_guess][col_guess] in ["💥", "❌"]:
                print("SPOT GUESSED")
                continue
            if "🛥️" in board[row_guess][col_guess]:
                print("HIT")
                #playsound('hit_sound.wav')
                board[row_guess][col_guess] = "💥"
                hid_board[row_guess][col_guess] = "💥"
                break
            elif board[row_guess][col_guess] == "🌊":
                print("MISS!")
                #playsound('miss_sound.wav')
                board[row_guess][col_guess] = "❌"
                hid_board[row_guess][col_guess] = "❌"
                break
        else:
            print("INVALID SPOT, TRY AGAIN")

def comp_guess(board, hid_board):
    while True:
        row_guess = random.randrange(0,5)
        col_guess = random.randrange(0,5)

        if hid_board[row_guess][col_guess] in ["💥", "❌"]:
            continue
        if "🛥️" in board[row_guess][col_guess]:
            print("THE COMPUTER HIT")
            #playsound('hit_sound.wav')
            board[row_guess][col_guess] = "💥"
            hid_board[row_guess][col_guess] = "💥"
            break
        elif board[row_guess][col_guess] == "🌊":
            print("THE COMPUTER MISSED")
            #playsound('miss_sound.wav')
            board[row_guess][col_guess] = "❌"
            hid_board[row_guess][col_guess] = "❌"
            break
        
def next_turn():
    input("CLICK 'ENTER' KEY BEFORE PASSING THE COMPUTER TO OTHER USER: ")
    for i in range(100):
        print("\n")

def check_win(board, player_num, ship_amt):
    hits = sum(row.count("💥") for row in board)
    if hits == ship_amt:
        #playsound('winner.wav')
        sys.exit(f"PLAYER {player_num} WINS")

def two_player(board_p1, board_p2, hid_board_p1, hid_board_p2):
    while True:
        try:
            ship_amt = int(input("HOW MANY SHIPS WOULD YOU LIKE TO PLACE? (1-10): "))
            if 1 <= ship_amt <= 10:
                break
            else:
                print("NUMBER 1-10")
        except ValueError:
            print("NUMBER ONLY")

    while True:
        try:
            choose_first = int(input("PICK A NUMBER 1 OR 2 TO DECIDE WHO GOES FIRST: "))
            if 1 <= choose_first <= 2:
                break
            else:
                print("NUMBER 1 OR 2 ONLY")
        except ValueError:
            print("NUMBER ONLY")

    rand = random.randint(1, 2)
    print("\nTHE RANDOM NUMBER IS...")
    time.sleep(.5)
    print(rand)
    if choose_first == rand:
        print("\nTHE USER WHO GUESSED IS USER 1, THEY WILL GO FIRST")
    else:
        print("\nTHE USER WHO GUESSED IS USER 2, THEY WILL GO SECOND, PASS COMPUTER TO PLAYER 1")
    
    print("\nPLAYER 1, PLACE SHIPS")
    show_board(board_p1, 1)
    player_pieces(board_p1, 1, ship_amt)
    next_turn()

    print("\nPLAYER 2, PLACE SHIPS")
    show_board(board_p2, 2)
    player_pieces(board_p2, 2, ship_amt)
    next_turn()

    while True:
        show_board(hid_board_p2, 1) 
        guess_ship(board_p2, hid_board_p2, 1)
        check_win(hid_board_p2, 1, ship_amt)
        next_turn()

        show_board(hid_board_p1, 2)  
        guess_ship(board_p1, hid_board_p1, 2)
        check_win(hid_board_p1, 2, ship_amt)
        next_turn()

def single_player(board_p1, board_p2, hid_board_p1, hid_board_p2):
    while True:
        try:
            ship_amt = int(input("HOW MANY SHIPS WOULD YOU LIKE TO PLACE? (1-10): "))
            if 1 <= ship_amt <= 10:
                break
            else:
                print("NUMBER 1-10")
        except ValueError:
            print("NUMBER ONLY")

    print("\nPLAYER 1, PLACE SHIPS")
    show_board(board_p1, 1)
    player_pieces(board_p1, 1, ship_amt)
    
    print("\nCOMPUTER IS PLACING ITS PIECES")
    time.sleep(3)
    comp_pieces(board_p2, ship_amt)

    while True:
        print("\nPLAYER 1's TURN")
        show_board(hid_board_p2, 2) 
        guess_ship(board_p2, hid_board_p2, 1)
        show_board(hid_board_p2, 2)
        check_win(hid_board_p2, 1, ship_amt)
        
        print("\nCOMPUTER'S TURN")
        time.sleep(2)
        comp_guess(board_p1, hid_board_p1)
        show_board(hid_board_p1, 1)  
        check_win(hid_board_p1, 2, ship_amt)


while True:
    #playsound('welcome.wav')
    print("WELCOME TO BATTLESHIP!")
    welcome = input("WOULD YOU LIKE TO PLAY WITH 1 OR 2 PLAYERS? ")
    if welcome == "1":
        single_player(board_p1, board_p2, hid_board_p1, hid_board_p2)
    elif welcome == "2":
        two_player(board_p1, board_p2, hid_board_p1, hid_board_p2)
    else:
        print("INVALID INPUT!")
