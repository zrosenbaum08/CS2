'''
Author: Zac Rosenbaum
Date: 5/1/2025
Description: Creates 1 player and 2 player battleship
Features: choose ship amount, plays sound, dots look like battleships
Bugs: None
'''
import sys
import random
import time
from playsound import playsound

board_p1 = [["🌊"] * 5 for i in range(5)]        #creates board for player 1
hid_board_p1 = [["🌊"] * 5 for i in range(5)]    #creates board to show to player 2
board_p2 = [["🌊"] * 5 for i in range(5)]        #creates board for player 2
hid_board_p2 = [["🌊"] * 5 for i in range(5)]    #creates baord to show player 1

def show_board(board, player_num):
    '''
    Displays player's board with row and column
    Args:
        board (list) list which is the board.
        player_num (int) Player number (1 or 2).
    Returns:
        None
    '''
    print(f"PLAYER {player_num}'s BOARD:")
    print("   1  2  3  4  5")
    row_num = 1
    for row in board:
        print(str(row_num) + " " + ' '.join(row))   #prints out the board with the row number
        row_num += 1

def player_pieces(board, player, ship_amt):
    '''
    Let player place ships 
    Args:
        board (list) board to place ships on.
        player (int) Player num
        ship_amt (int) number of ships to place.
    Returns:
        None
    '''
    ships = 0
    print(f"PLAYER: {player}, PLACE SHIPS")
    while ships < ship_amt:     #continues while ships is less than what should be
        try:                    #trys the following
            row = int(input("Which row? (1-5): ")) - 1      #sets user input -1 to get the cordinate
            col = int(input("Which column? (1-5): ")) - 1   #sets user input -1 to get the cordinate
        except ValueError:          #except user input of a character not an int
            print("NUMBER ONLY")
            continue
        if 0 <= row <= 4 and 0 <= col <= 4 and board[row][col] == "🌊":      #makes sure user input is between 0-4
            board[row][col] = "🛥️ "    #sets board cord to boat     
            ships += 1
            show_board(board, player)   #shows the user the board
        else:
            print("INVALID SPOT, TRY AGAIN")

def comp_pieces(board, ship_amt):
    '''
    Randomly places ships on board for single player
    Args:
        board (list) board to place ships on
        ship_amt (int)number of ships to place
    Returns:
        None
    '''
    ships = 0
    while ships < ship_amt:         #continous loop while ships placed is less than what it should be
        row = random.randint(0, 4)  #random number for computer play 0-4
        col = random.randint(0, 4)  #random number for computer play 0-4
        if board[row][col] == "🌊":  #checks if spot is unused
            board[row][col] = "🛥️ "
            ships += 1

def guess_ship(board, hid_board, player_num):
    '''
    for user to guess opponenets ships
    Args:
        board (list) Opponents real board
        hid_board (list) player's view of opponent's board / hides the ships
        player_num (int)p layer number making the guess
    Returns:
        None
    '''
    print(f"PLAYER: {player_num} GUESS SPOT")
    while True:
        try:                                                    #tries
            row_guess = int(input("Which row? (1-5): ")) - 1    #sets user input -1 to get the cordinate
            col_guess = int(input("Which column? (1-5): ")) - 1 #sets user input -1 to get the cordinate
        except ValueError:                                      #excepts value error
            print("NUMBER ONLY")                                
            continue

        if 0 <= row_guess <= 4 and 0 <= col_guess <= 4:         #makes sure int is within 0-4
            if hid_board[row_guess][col_guess] in ["💥", "❌"]: #checks if spot is already used
                print("SPOT GUESSED")
                continue
            if "🛥️" in board[row_guess][col_guess]:             #checks if the boat is in the spot (hit)
                print("HIT")
                playsound('hit_sound.wav')                          #plays wav file
                board[row_guess][col_guess] = "💥"                   #sets both boards to explosion instead of ship
                hid_board[row_guess][col_guess] = "💥"
                break
            elif board[row_guess][col_guess] == "🌊":                #checks if the spot is water (miss)
                print("MISS!")
                playsound('miss_sound.wav')                          #plays wav file
                board[row_guess][col_guess] = "❌"                   #sets the board to miss
                hid_board[row_guess][col_guess] = "❌"
                break
        else:
            print("INVALID SPOT, TRY AGAIN")

def comp_guess(board, hid_board):
    '''
    Makes a random guess for the computer
    Args:
        board (list) player's actual board
        hid_board (list) comps view of player's board
    Returns:
        None
    '''
    while True:
        row_guess = random.randrange(0,5)           #random number 0-4
        col_guess = random.randrange(0,5)           #random number 0-4 for computer guessing the ship

        if hid_board[row_guess][col_guess] in ["💥", "❌"]:   #checks if spot is guess
            continue                                            #redoes the loop
        if "🛥️" in board[row_guess][col_guess]:             #checks if 
            print("THE COMPUTER HIT")
            playsound('hit_sound.wav')                          #plays wav file
            board[row_guess][col_guess] = "💥"                  #sets board spot to explosion
            hid_board[row_guess][col_guess] = "💥"
            break
        elif board[row_guess][col_guess] == "🌊":
            print("THE COMPUTER MISSED")
            playsound('miss_sound.wav')                          #plays wav file
            board[row_guess][col_guess] = "❌"                  #sets the spot on both boards to signal a missed ship
            hid_board[row_guess][col_guess] = "❌"
            break
        
def next_turn():
    '''
    clears screen for next player.
    Args:
        None
    Returns:
        None
    '''
    input("CLICK 'ENTER' KEY BEFORE PASSING THE COMPUTER TO OTHER USER: ")
    for i in range(500):    #makes 500 line breaks so the user cant see the other persons baord
        print("\n") 

def check_win(board, player_num, ship_amt):
    '''
    Checks if win condition met to close game
    Args:
        board (list) players board to check hits on
        player_num (int): Player number
        ship_amt (int): Total ships placed
    Returns:
        None
    '''
    hits = sum(row.count("💥") for row in board)        #sets hits to the amt of hit emojis on the board
    if hits == ship_amt:
        playsound('winner.wav')                         #plays wav file
        sys.exit(f"PLAYER {player_num} WINS")           #says someone wins

def two_player(board_p1, board_p2, hid_board_p1, hid_board_p2):
    '''
    full 2-player game loop
    Args:
        board_p1 (list) P1's actual board
        board_p2 (list) p2's actual board
        hid_board_p1 (list) hidden version of Player 1's board
        hid_board_p2 (list) hidden version of Player 2's board

    Returns:
        None
    '''
    while True:
        try:
            ship_amt = int(input("HOW MANY SHIPS WOULD YOU LIKE TO PLACE? (1-20): ")) #ask for ship amt 
            if 1 <= ship_amt <= 20: #makes sure user put a max of 20 ships
                break
            else:
                print("NUMBER 1-20")   
        except ValueError:  #excepts a non int input
            print("NUMBER ONLY")

    while True:
        try:
            choose_first = int(input("PICK A NUMBER 1 OR 2 TO DECIDE WHO GOES FIRST: "))
            if 1 <= choose_first <= 2:  #checks to see if num is 1 or 2
                break
            else:
                print("NUMBER 1 OR 2 ONLY")
        except ValueError:              #excepts non int input and asks again
            print("NUMBER ONLY")

    rand = random.randint(1, 2)     #generates a random number
    print("\nTHE RANDOM NUMBER IS...")
    time.sleep(.5)
    print(rand)     #prints rand num
    if choose_first == rand:        #checks if rand num is the same as the guessed num
        print("\nTHE USER WHO GUESSED IS USER 1, THEY WILL GO FIRST")
    else:
        print("\nTHE USER WHO GUESSED IS USER 2, THEY WILL GO SECOND, PASS COMPUTER TO PLAYER 1")
    
    print("\nPLAYER 1 PLACE SHIPS") #begins the game
    show_board(board_p1, 1)     #shows user 1 baord before placing ships
    player_pieces(board_p1, 1, ship_amt)    #places ships
    next_turn()

    print("\nPLAYER 2 PLACE SHIPS")
    show_board(board_p2, 2)
    player_pieces(board_p2, 2, ship_amt)
    next_turn()

    while True:
        show_board(hid_board_p2, 2)         #shows hidden baord before guessing ships 
        guess_ship(board_p2, hid_board_p2, 1)       #guesses ships
        check_win(hid_board_p2, 1, ship_amt)        #checks if user 1 wins
        next_turn()

        show_board(hid_board_p1, 1)  
        guess_ship(board_p1, hid_board_p1, 2)
        check_win(hid_board_p1, 2, ship_amt)
        next_turn()

def single_player(board_p1, board_p2, hid_board_p1, hid_board_p2):
    '''
    Runs the full single-player game 
    Args:
        board_p1 (list) players actual board
        board_p2 (list): computers actual board
        hid_board_p1 (list): Hidden version of players board
        hid_board_p2 (list): Hidden version of computers board
    Returns:
        None
    '''
    while True:
        try:
            ship_amt = int(input("HOW MANY SHIPS WOULD YOU LIKE TO PLACE? (1-20): "))
            if 1 <= ship_amt <= 20:     #checks ship amt
                break
            else:
                print("NUMBER 1-20")
        except ValueError:  #re asks question if given non int input
            print("NUMBER ONLY")

    print("\nPLAYER 1, PLACE SHIPS")    
    show_board(board_p1, 1) #shows baord to place ships
    player_pieces(board_p1, 1, ship_amt)
    
    print("\nCOMPUTER IS PLACING ITS PIECES")
    time.sleep(3)
    comp_pieces(board_p2, ship_amt) #computer places random peices

    while True:
        print("\nPLAYER 1's TURN")
        show_board(hid_board_p2, 2) #shows hid board
        guess_ship(board_p2, hid_board_p2, 1)   #user guesses ships
        show_board(hid_board_p2, 2)             #shows computer board again
        check_win(hid_board_p2, 1, ship_amt)    #checks to see if user won   
        
        print("\nCOMPUTER'S TURN")
        time.sleep(2)
        comp_guess(board_p1, hid_board_p1)  #computer guesses
        show_board(hid_board_p1, 1)         #displays new baord
        check_win(hid_board_p1, 2, ship_amt)    #checks if computer won


while True:
    playsound('welcome.wav')        #plays wav file
    print("WELCOME TO BATTLESHIP!")
    welcome = input("WOULD YOU LIKE TO PLAY WITH 1 OR 2 PLAYERS? ") #asks for 1 or 2 players
    if welcome == "1":
        single_player(board_p1, board_p2, hid_board_p1, hid_board_p2)   #runs 1 player
    elif welcome == "2":
        two_player(board_p1, board_p2, hid_board_p1, hid_board_p2)      #runs 2 player
    else:
        print("INVALID INPUT!")
