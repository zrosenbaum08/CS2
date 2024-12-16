'''
Author: Zac Rosenbaum
Date: 12/20/2024
Description: allows user to play hangman by a random word
Features: None
Bugs: None
Sources:
Class
https://www.shecodes.io/athena/12032-how-to-replace-spaces-with-dashes-in-a-python-string
https://www.simplilearn.com/tutorials/python-tutorial/list-to-string-in-python
'''
import random   #random library
import sys      #imports sys
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
guessed_letter = []     #empty list 

word_list = []  # creates list from txt
f = open("words.txt", "r")  #read mode for txt
for line in f:              #for each line in the txt
    line = line.strip()     #get rid of leading and trailing spaces
    word_list.append(line)  #adds each word to the list

secret_word = random.choice(word_list).lower()  # andom word from list
guessed_word = ["_"] * len(secret_word)         #list of _ for the length of the word
board_word = " ".join(guessed_word)             # adds a space between the underscores so user can see word length


lives = 6                           #sets user lives 6
print("WELCOME TO HANGMAN!")        #welcome to hangman

def board_help(lives, guessed_letter):
    """
    shows all the info needed to play
    Args:
        lives user has, letters user has guessed
    Returns:
        prints all the info (lives, guessed word, letters guessed)
    """
    print(f"\nYOU HAVE {lives} LIVES")  # print the amount of lives user has
    print("Word: " + " ".join(guessed_word))  # shows the word with _ _ _ _ _
    print("Guessed letters:  " + ' '.join(guessed_letter) + "\n") # prints the guessed letters as string

def ask_user(alphabet, guessed_letter, secret_word, lives):
    """
    asks user for a letter and checks if it's in the hidden word
    Args:
        alhpabet (a,b,c,d,e,f...) guessed letter (letters the user has guessed) secret word (random word that they are guessing) amt of lives they have
    Returns:
        returns new lives
    """
    while True:  # loop
        guess = str.lower(input("What letter would you like to guess?:  "))  # asks user for letter to guess
        if guess in alphabet:  # if the input is in alphabet
            guessed_letter.append(guess)    #adds guess to guessed letter list
            alphabet.remove(guess)          #remove guess from alphabet 
            break                           #breaks the loop
        else:                               #else (not in alphabet or in guessed letters already)
            print("Please input ONE letter ONLY and you may only guess a letter ONCE.")     #tells user only one letter and only one guess per letter

    if guess in secret_word:                        #if the user geuss in secret word
        for i in range(len(secret_word)):           #for lenght in secret word
            if secret_word[i] == guess:             #if the secret word letter = giuessed letter
                guessed_word[i] = guess             #change the guessed letter to be visable instead of dashes
    
    else:                                           #if else/not insecret word
        print("THAT LETTER IS NOT A PART OF THE WORD")  #prints that guessed letter not in word
        lives -= 1                                      #one less life
    
    return lives                                        #returns updated lives (if needed)


gallows = ["""
           +---+
           |   |
               |
               |
               |
               |
        ========
        """, """
           +---+
           |   |
           O   |
               |
               |
               |
        ========
        """, """
           +---+
           |   |
           O   |
           |   |
               |
               |
        ========
        """, """
           +---+
           |   |
           O   |
          /|   |
               |
               |
        ========
        """, """
           +---+
           |   |
           O   |
          /|\  |
               |
               |
        ========
        """, """
           +---+
           |   |
           O   |
          /|\  |
          /    |
               |
        ========
        """, """
           +---+
           |   |
           O   |
          /|\  |
          / \  |
               |
        ========
        """]  #art for gallows

def board_change(lives):
    """
    prints the board based on user lives
    Args:
        lives (amt of lives user has)
    Returns:
        prints the new board
    """
    if lives == 6:              #if lives is 6, 
        print(gallows[0])       #prints the 1st gallow
    elif lives == 5:            #if lives is 5, 
        print(gallows[1])       #prints the 2nd gallow       
    elif lives == 4:            #if lives is 4, 
        print(gallows[2])       #prints the 3rd gallow
    elif lives == 3:            #if lives is 3, 
        print(gallows[3])       #prints the 4th gallow
    elif lives == 2:            #if lives is 2, 
        print(gallows[4])       #prints the 5th gallow
    elif lives == 1:            #if lives is 1, 
        print(gallows[5])       #prints the 6th gallow
    elif lives == 0:            #if lives is 0, 
        print(gallows[6])       #prints the 7th gallow

def game_play(lives, guessed_letter, alphabet, secret_word):
    """
    carries out the full game
    Args:
        lives (amt of lives user has), the letters user guessed, alphabet, word user is trying to guess
    Returns:
        win or lose
    """
    while True:                             #loop
        board_help(lives, guessed_letter)   #carries out the baord help function to show user the lives, word, etc
        board_change(lives)                 #carries out the board change func to show the new board
        lives = ask_user(alphabet, guessed_letter, secret_word, lives)  #sets lives to the ask user func that asks user to guess
        if not "_" in guessed_word:         #if _ not in the guessed word (win)
            print(f"THE WORD WAS {secret_word}") #prints out the word
            sys.exit("YOU WON")             #exits the game and tells the user they won
        elif lives == 0:                    #else if lives is 0 (loss)
            print(f"THE WORD WAS {secret_word}") #prints out the word
            sys.exit("YOU LOST")            #exits game and tells user they lost
        else:                               #else 
            continue                        #goes through loop again

game_play(lives, guessed_letter, alphabet, secret_word)     #carries ou the game play func to carry out the full game