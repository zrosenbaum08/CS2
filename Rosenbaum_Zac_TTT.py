'''
Author: Zac Rosenbaum
Date: 11/30/2024
Description: allows a user to play tic-tac-toe agianst either another person or the computer, which plays in a random location
Features: None
Bugs: None
Sources: Class lectures
'''
import random   #imports the random library
import sys      #imports sys library

box = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]                   #creates the board
def show_board():
    """
    shows the ttt board
    Args:
        none
    Returns:
        just prints the board
    """   
    for i in range(len(box)):                   #for index in the length of the box
        for j in range(len(box[i])):            #for index in each row
            print(box[i][j], end = '  ')        #prints all cordinates
        print()

def turn_play(player):
    """
    allow the player to pick a spot on the board and changes to board
    Args:
        player or the int the cordinate where the player wanted to play
    Returns:
        a corrected board
    """
    while True:                                 #creates a loop
            where_play = input('''
Where would you like to play?   ''')            #asks user where they would like to play as an interger
            try:                                #checks if the indected code works
                int(where_play)                 #sets user input as an interger
            except ValueError:                  #excepts values errors
                print("MUST INPUT A NUMBER!")   #tells user only numbers must be inputed
            if where_play == "1":                 #if user inputs 1
                if box[0][0] == "X" or box[0][0] == "O":      #checks if spot is already taken
                    print("spot has already been picked")     #tells user spot is taken
                else:                                         #else
                    box[0][0] = player                        #sets specific box to that players letter
                    show_board()            #runs the show board function to show the users where to play
                    break                    #breaks loop
            elif where_play == "2":                 #if user inputs 2
                if box[0][1] == "X" or box[0][1] == "O":      #checks if spot is already taken
                    print("spot has already been picked")     #tells user spot is taken
                else:                                         #else 
                    box[0][1] = player                        #sets specific box to that players letter
                    show_board()            #runs the show board function to show the users where to play
                    break                    #breaks loop
            elif where_play == "3":                 #if user inputs 3
                if box[0][2] == "X" or box[0][2] == "O":      #checks if spot is already taken
                    print("spot has already been picked")     #tells user spot is taken
                else:                                         #else
                    box[0][2] = player                        #sets specific box to that players letter
                    show_board()            #runs the show board function to show the users where to play
                    break                    #breaks loop
            elif where_play == "4":                 #if user inputs 4
                if box[1][0] == "X" or box[1][0] == "O":      #checks if spot is already taken
                    print("spot has already been picked")     #tells user spot is taken
                else:                                         #else
                    box[1][0] = player                        #sets specific box to that players letter
                    show_board()            #runs the show board function to show the users where to play
                    break                    #breaks loop
            elif where_play == "5":                 #if user inputs 5
                if box[1][1] == "X" or box[1][1] == "O":      #checks if spot is already taken
                    print("spot has already been picked")     #tells user spot is taken
                else:                                         #else
                    box[1][1] = player                        #sets specific box to that players letter
                    show_board()            #runs the show board function to show the users where to play
                    break                    #breaks loop
            elif where_play == "6":                 #if user inputs 6
                if box[1][2] == "X" or box[1][2] == "O":      #checks if spot is already taken
                    print("spot has already been picked")     #tells user spot is taken
                else:                                         #else
                    box[1][2] = player                        #sets specific box to that players letter
                    show_board()            #runs the show board function to show the users where to play
                    break                    #breaks loop
            elif where_play == "7":                 #if user inputs 7
                if box[2][0] == "X" or box[2][0] == "O":      #checks if spot is already taken
                    print("spot has already been picked")     #tells user spot is taken
                else:                                         #else
                    box[2][0] = player                        #sets specific box to that players letter
                    show_board()            #runs the show board function to show the users where to play
                    break                    #breaks loop
            elif where_play == "8":                 #if user inputs 8
                if box[2][1] == "X" or box[2][1] == "O":      #checks if spot is already taken
                    print("spot has already been picked")     #tells user spot is taken
                else:                                         #else
                    box[2][1] = player                        #sets specific box to that players letter
                    show_board()            #runs the show board function to show the users where to play
                    break                    #breaks loop
            elif where_play == "9":                 #if user inputs 9
                if box[2][2] == "X" or box[2][2] == "O":      #checks if spot is already taken
                    print("spot has already been picked")     #tells user spot is taken
                else:                                         #else
                    box[2][2] = player                        #sets  specific box to that players letter
                    show_board()            #runs the show board function to show the users where to play
                    break                   #breaks loop
            else:                           #else
                print("numbers 1-9 only!")  #tells user to only input numbers 1-9
                show_board()                #shows the board 
def comp_play():
    """
    creates a random number to play a random spot on the board
    Args:
        none
    Returns:
        new board
    """
    while True:                          #creates loop
        rand_spot = random.randint(1,9)  #creates a random number 1-9 called rand_spot
        if rand_spot == 1:            #if the random number is 1
            if box[0][0] == "X" or box[0][0] == "O":    #if spot is taken
                continue                                #runs the loop again
            else:                       #else
                box[0][0] = "O"         #sets specific box to make it O
                show_board()            #runs the show board function to show the users where to play
                break                   #breaks loop
        elif rand_spot == 2:            #else if the random number is 2
            if box[0][1] == "X" or box[0][1] == "O":    #if spot is taken
                continue                                #runs the loop again
            else:                       #else
                box[0][1] = "O"         #sets specific box to make it O
                show_board()            #runs the show board function to show the users where to play
                break                   #breaks loop
        elif rand_spot == 3:            #else if the random number is 3
            if box[0][2] == "X" or box[0][2] == "O":    #if spot is taken
                continue                                #runs the loop again
            else:                       #else
                box[0][2] = "O"         #sets specific box to make it O
                show_board()            #runs the show board function to show the users where to play
                break                   #breaks loop
        elif rand_spot == 4:            #else if the random number is 4
            if box[1][0] == "X" or box[1][0] == "O":    #if spot is taken
                continue                                #runs the loop again
            else:                       #else
                box[1][0] = "O"         #sets specific box to make it O
                show_board()            #runs the show board function to show the users where to play
                break                   #breaks loop
        elif rand_spot == 5:            #else if the random number is 5
            if box[1][1] == "X" or box[1][1] == "O":    #if spot is taken
                continue                                #runs the loop again
            else:                       #else
                box[1][1] = "O"         #sets specific box to make it O
                show_board()            #runs the show board function to show the users where to play
                break                   #breaks loop
        elif rand_spot == 6:            #else if the random number is 6
            if box[1][2] == "X" or box[1][2] == "O":    #if spot is taken
                continue                                #runs the loop again
            else:                       #else
                box[1][2] = "O"         #sets specific box to make it O
                show_board()            #runs the show board function to show the users where to play
                break                   #breaks loop
        elif rand_spot == 7:            #else if the random number is 7
            if box[2][0] == "X" or box[2][0] == "O":    #if spot is taken
                continue                                #runs the loop again
            else:                       #else
                box[2][0] = "O"         #sets specific box to make it O
                show_board()            #runs the show board function to show the users where to play
                break                   #breaks loop
        elif rand_spot == 8:            #else if the random number is 8
            if box[2][1] == "X" or box[2][1] == "O":    #if spot is taken
                continue                                #runs the loop again
            else:                       #else
                box[2][1] = "O"         #sets specific box to make it O
                show_board()            #runs the show board function to show the users where to play
                break                   #breaks loop
        elif rand_spot == 9:            #else if the random number is 9
            if box[2][2] == "X" or box[2][2] == "O":    #if spot is taken
                continue                                #runs the loop again
            else:                       #else
                box[2][2] = "O"         #sets specific box to make it O
                show_board()            #runs the show board function to show the users where to play
                break                   #breaks loop
        


def run_2game():
    """
    Runs the 2 player game
    Args:
        none
    Returns:
        a winner of the game
    """             
    show_board()        #shows the current board by running the show_board func
    turn_play("X")      #runs the turn_play func to let the x player play
    print("Now player O, it is your turn")      #displays that it is now O's turn
    turn_play("O")      #runs the turn_play func to let the o player play
    turn_play("X")      #runs the turn_play func to let the x player play
    turn_play("O")      #runs the turn_play func to let the o player play
    turn_play("X")      #runs the turn_play func to let the x player play
    check_win(box)      #runs the check win function taking in the new baord to see if anyone ahs won yet
    turn_play("O")      #runs the turn_play func to let the o player play
    check_win(box)      #runs the check win function taking in the new baord to see if anyone ahs won yet
    turn_play("X")      #runs the turn_play func to let the x player play
    check_win(box)      #runs the check win function taking in the new baord to see if anyone ahs won yet
    turn_play("O")      #runs the turn_play func to let the o player play
    check_win(box)      #runs the check win function taking in the new baord to see if anyone ahs won yet
    turn_play("X")      #runs the turn_play func to let the x player play
    check_win(box)      #runs the check win function taking in the new baord to see if anyone ahs won yet
    if check_win(box) == "no winner yet":   #if the check win func returns no winner
        print("the game is a tie")          #prints that the game ends as a tie

def check_win(box):
    """
    checks if the game has been won by anyone
    Args:
        takes in the box to see if there are any 3-in-a-row
    Returns:
        a winner of the game or it is a tie
    """   
    if box[0][0] == box[0][1] and box[0][1] == box[0][2]:     #checks win horisontal top
        if box[0][0] == "X":                    #if the boxes is = to X,
            sys.exit("X IS THE WINNER")         #exits and says X is the winner
        else:                                   #else 
            sys.exit("O IS THE WINNER")         #exits and says O is the winner
    elif box[1][0] == box[1][1] and box[1][1] == box[1][2]:     #checks win horisontal middle
        if box[1][0] == "X":                    #if the boxes is = to X,
            sys.exit("X IS THE WINNER")         #exits and says X is the winner
        else:                                   #else 
            sys.exit("O IS THE WINNER")         #exits and says O is the winner
    elif box[2][0] == box[2][1] and box[2][1] == box[2][2]:     #checks win horisontal bottom
        if box[2][0] == "X":                    #if the boxes is = to X,
            sys.exit("X IS THE WINNER")         #exits and says X is the winner
        else:                                   #else 
            sys.exit("O IS THE WINNER")         #exits and says O is the winner
    elif box[0][0] == box[1][1] and box[1][1] == box[2][2]:     #checks win diagonal left to right
        if box[0][0] == "X":                    #if the boxes is = to X,
            sys.exit("X IS THE WINNER")         #exits and says X is the winner
        else:                                   #else 
            sys.exit("O IS THE WINNER")         #exits and says O is the winner
    elif box[0][2] == box[1][1] and box[1][1] == box[2][0]:     #checks win diagonal right to left
        if box[0][2] == "X":                    #if the boxes is = to X,
            sys.exit("X IS THE WINNER")         #exits and says X is the winner
        else:                                   #else 
            sys.exit("O IS THE WINNER")         #exits and says O is the winner
    elif box[0][0] == box[1][0] and box[1][0] == box[2][0]:     #checks win vertical left    
        if box[0][0] == "X":                    #if the boxes is = to X,
            sys.exit("X IS THE WINNER")         #exits and says X is the winner
        else:                                   #else 
            sys.exit("O IS THE WINNER")         #exits and says O is the winner
    elif box[0][1] == box[1][1] and box[1][1] == box[2][1]:     #checks win vertical middle
        if box[0][1] == "X":                    #if the boxes is = to X,
            sys.exit("X IS THE WINNER")         #exits and says X is the winner
        else:                                   #else 
            sys.exit("O IS THE WINNER")         #exits and says O is the winner
    elif box[0][2] == box[1][2] and box[1][2] == box[2][2]:     #checks win vertical right
        if box[0][2] == "X":                    #if the boxes is = to X,
            sys.exit("X IS THE WINNER")         #exits and says X is the winner
        else:                                   #else      
            sys.exit("O IS THE WINNER")         #exits and says O is the winner
    else:                                       #else
        return("no winner yet")                 #returns no winner yet

def run_1game():
    """
    Runs the 1 player game
    Args:
        none
    Returns:
        a winner of the game/tie
    """                
    show_board()        #shows the current board by running the show_board func
    turn_play("X")      #runs the turn_play func to let the x player play
    print("\n")         #prints space
    comp_play()         #runs the comp_play func for the computer to play agaisnt the player
    turn_play("X")      #runs the turn_play func to let the x player play
    print("\n")         #prints space
    comp_play()         #runs the comp_play func for the computer to play agaisnt the player
    turn_play("X")      #runs the turn_play func to let the x player play
    check_win(box)      #runs the check win function taking in the new baord to see if anyone ahs won yet
    print("\n")         #prints space
    comp_play()         #runs the comp_play func for the computer to play agaisnt the player
    check_win(box)      #runs the check win function taking in the new baord to see if anyone ahs won yet
    turn_play("X")      #runs the turn_play func to let the x player play
    check_win(box)      #runs the check win function taking in the new baord to see if anyone ahs won yet
    print("\n")         #prints space
    comp_play()         #runs the comp_play func for the computer to play agaisnt the player
    check_win(box)      #runs the check win function taking in the new baord to see if anyone ahs won yet
    turn_play("X")      #runs the turn_play func to let the x player play
    check_win(box)      #runs the check win function taking in the new baord to see if anyone ahs won yet
    if check_win(box) == "no winner yet":   #if the check win func returns no winner
        print("the game is a tie")          #prints that the game ends as a tie

def main():
    """
    Runs the entire game 
    Args:
        none
    Returns:
        a winner of the game/tie
    """   
    play_game = str.lower(input('''
    WELCOME! WOULD YOU LIKE TO PLAY TIC-TAC-TOE? (yes or no):  '''))    #asks user if they want to play TTT
    if play_game == "yes" or play_game == "y" or play_game == "sure" or play_game == "ok":       #if user says yes
        while True:
            two_or_one = str.lower(input('''
    Would you like to play with 1 (against computer) or 2 players:  '''))                  #Asks user if they would like to play with 1 player or 2
            
            if two_or_one == "1" or two_or_one == "one":                    #if else if player wants to play single player    
                print("Player goes first")                                  #lets the player go before the computer
                run_1game()                                                 #runs the single player game
                break
            elif two_or_one == "2" or two_or_one == "two":                  #if user says 2
                while True:                                                 #creates a continous loop until broken
                    rand_play = int(input('''
    Player 1 calls the cointoss, pick a number 1 or 2:  '''))           #asks user 1 for random number 
                    if rand_play == 1 or rand_play == 2:    #if user either inputs 1 or 2
                        break                               #breaks the continous loop
                    else:                                   #else
                        print("User must input either '1' or '2'")      #displays that user must either input 1 or 2
                rand_play_num = random.randint(1,2)                     #creates random number either 1 or 2
                print(f'''
    The coin toss says: {rand_play_num}''')                             #prints the random number
                if rand_play == rand_play_num:                          #if user number is euqal to random number
                    print("Player 1 you are X, go first")               #print player 1 (who picked the number) goes first
                    run_2game()                                         #runs the 2 player game
                    break
                else:                                                   #else
                    print("Player 2 you are X, go first")               #tells player two to go first
                    run_2game()                                         #runs the 2 player game
                    break
            else:
                print("Only 1 or 2 players")    #tells user that you can only choose 1-2 players

    else:                                      #else
        sys.exit("bye")                        #prints bye and exits the program (player doesn't want to play TTT)

main()          #runs the main func