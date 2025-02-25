'''
Author: Zac Rosenbaum
Date: 2/28/2025
Description: Creates functions to recreate some functions in the string class
Features: A few bonus functions
Bugs: None
Sources:
Class
https://www.geeksforgeeks.org/python-ways-to-sort-letters-of-string-alphabetically/
https://www.w3schools.com/python/python_howto_reverse_string.asp 
'''
import random
alpha = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]  #list for alphabet(isalpha)
alpha_cap = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
conts_alpha = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "z"]#list of conts
vowel_alpha = ["a", "e", "i", "o", "u", "y"] #list of vowel
name_titles = ["Dr.",'Dr', 'Doctor', 'Reverend', 'Sr', 'Senior', 'Professor', 'Private', 'Private second class', 'Private first class', 'Specialist', 'Corporal', 'Sergeant', ' Staff sergeant', 'Sergeant first class', 'Master sergeant', 'First sergeant', 'Sergeant major', 'Command sergeant major', 'Sergeant major', 'Second lieutenant', 'First lieutenant', 'Captain', 'Major','Lieutenant colonel', 'Colonel', 'Brigadier general', 'Major general', "Mr.", "Mrs.", "Ms.", "Sir", "Lord", "Lady", "Prof", "Representative", "Senator", "President", "Vice-President", "King", "Queen", "Prince", "Princess",]#list of titles for names


while True:                                             #loop
    name = input("Please Enter Your Full Name:   ")     #asks user for name
    try:                                                #checks
        name_list = name.split(' ')                     #if the name can be split by spaces
        break                                           #breaks loop
    except ValueError:                                  #accepts if user inputs numbers
        print("TRY AGAIN, MUST BE LETTERS")             #prints that user must input letters

def name_find(name_list, name_titles):
    """
    separates the name into first, middle, last and title
    Args:
        user name input as list and title list
    Returns:
        first name, middle name, last name, title
    """
    title = []              #sets title equal to empty list
    first = []              #sets first equal to empty list
    middle = []              #sets middle equal to empty list
    last = []              #sets last equal to empty list

    if name_list[0] in name_titles or "." in name_list[0]:  #checks in the first elmt in list is in the title list (name titles) or in a period is in their name
        title = name_list.pop(0)            #removes the first element of the list and assigns to name title

    first = name_list.pop(0)        #removes the first element of the list and assigns to first name

    if len(name_list) > 1:          #if length of name list is greater than 1
        middle = name_list[:-1]     #takes all values til 2nd to last and sets them to middle names
        last = name_list.pop(-1)    #removes the last element of the list and assigns to last name
    elif len(name_list) == 1:       #else if len is 1,
        last = name_list.pop(0)     #removes the last element of the list and assigns to last name
    return title, first, middle, last       #returns all new variables

def func_1(name):
    """
    displays name backwards
    Args:
        name as string
    Returns:
        name backwards
    """
    return name[::-1]   #prints the full name backwards

def func_2(name):  
    """
    Finds frecuency of a vowel
    Args:
        name as string
    Returns:
        freceuncy of the vowel
    """
    frecuency = 0                                                       #sets frecuency variable to 0
    while True:                                                         #loop
        vowel_find = input("Please Enter a Vowel to Find Fequency:  ")  #asks user for a vowel
        vowel_find = func_8(vowel_find, alpha_cap, alpha)               #makes input lowercase
        new_name = func_8(name, alpha_cap, alpha)                       #makes the user name all lowerase
        if vowel_find in vowel_alpha:                                   #makes sure input is a vowel
            for i in new_name:                                          #for loop for each character
                if i == vowel_find:                                     #if character = the vowel
                    frecuency += 1                                      #add 1 to frecuency
                    
                else:                                                   #else
                    continue                                            #continue(go to next letter)
            return(f"The Frecuency of {vowel_find} in {name} is {frecuency}")   #returns the frecuency of that vowel
        else:                                                                   #else
            return("user must only input a single vowel")                       #returns that user must input vowel only

def func_3(name):  
    """
    Finds frecuency of a consonant
    Args:
        name as string
    Returns:
        freceuncy of the consonant
    """
    frecuency = 0                                                       #sets frecuency variable to 0                          
    while True:                                                         #loop
        const_find = input("Please Enter a Consonant to Find Fequency:  ")  #asks for consonant 
        const_find = func_8(const_find, alpha_cap, alpha)                   #makes input lowercase
        new_name = func_8(name, alpha_cap, alpha)                           #makes the user name all lowercase
        if const_find in conts_alpha:                                       #makes sure input is a consonant
            for i in new_name:                                              #for loop for each character
                if i == const_find:                                         #if character is equal to user consonant
                    frecuency += 1                                          #adds 1 to frecuency
                    
                else:                                                       #else      
                    continue                                                #goes to next loop
            return(f"The Frecuency of {const_find} in {name} is {frecuency}")   #returns the frecuency of that consonant
        else:                                                                   #else
            return("user must only input a single consonants")                  #returns that user must input consonant only
   
            
def func_4(first):  
    """
    Displays first name
    Args:
        first name as a string
    Returns:
        first name
    """
    return(f"First Name: {first}")         #returns first name                                               

def func_5(last):  
    """
    Displays last name
    Args:
        last name as a string
    Returns:
        last name
    """
    if len(last) > 0:                   #if length of lastname is > 0
        return(f"Last Name: {last}")    #returns last name
    else:                               #else
        return("No Last Name")          #returns no last name

def func_6(middle):
    """
    Displays middle name(s)
    Args:
        middle name as a list
    Returns:
        middle names
    """
    if len(middle) > 0:                 #if length of middle name list > 0 
        return(f"Middle Names: {', '.join(middle)}")    #returns middle names
    else:                                               #else
        return("No middle name")                        #returns no middle names

def func_7(last):  
    """
    returns boolean if last name has -
    Args:
        last name as a string
    Returns:
        true of false
    """
    return '-' in last      #returns t of f in - in last name

def func_8(name, alpha_cap, alpha):
    """
    makes name lowercase
    Args:
        name as a string, capital alphabet list, lowercase alphabet
    Returns:
        all low, string all lowercase
    """
    all_low = ""                            #sets all_low equal to empty string
    for letter in name:                     #for loop for amt of letters in name
        if letter in alpha_cap:             #checks if letter is capital
            idx = alpha_cap.index(letter)   #finds index of character
            all_low += alpha[idx]           #adds lowercase letter to all low
        else:                               #else
            all_low += letter               #adds character to all low
    return all_low                          #returns all low

def func_9(name, alpha_cap, alpha): 
    """
    makes name uppercase
    Args:
        name as a string, capital alphabet list, lowercase alphabet
    Returns:
        all cap, name string capitalized
    """
    all_cap = ""                            #sets all cap equal to empty string
    for letter in name:                     #for loop for amt of letters in name
        if letter in alpha:                 #checks if letter is lowercase
            idx = alpha.index(letter)       #finds index of character
            all_cap += alpha_cap[idx]       #adds capital letter with index to all cap
        else:                               #else
            all_cap += letter               #adds character to all cap
    return all_cap                          #returns all cap

def func_10(name, alpha_cap, alpha):   
    """
    randomizes order of characters
    Args:
        name as a string, capital alphabet list, lowercase alphabet
    Returns:
        rand_name string
    """
    rand_name = list(func_8(name, alpha_cap, alpha))        #makes list of all characters in name
    random.shuffle(rand_name)                               #shuffles the letters randomly
    return ''.join(rand_name)                               #returns randomized name

def func_11(first): 
    """
    checks if name is a palendrome
    Args:
       first name as a string
    Returns:
        true or false boolean
    """
    if func_8(first, alpha_cap, alpha)[::-1] == func_8(first, alpha_cap, alpha):    #checks if lowercase firstname is equal to the reverse lowercase first name
        return True                                                                 #returns true
    else:                                                                           #else
        return False                                                                #returns false

def func_12(name):
    """
    makes name in alphabetical order
    Args:
        name as a string
    Returns:
        name_order string in alhpabetical order
    """
    list = []                   #creates empty list
    l = len(name)               #sets variable "l" to length of name (not the number one*)
    for i in range (0,l):       #for loop only runs len name
        list.append(name[i])    #adds first character of name
    
    
    for i in range(0,l):        #for loop runs length of name
        for j in range(0,l):    #nested for loop runs lenght of name
            if list[i]<list[j]: #if list i is greater in value that list j
                list[i],list[j]=list[j],list[i]
    name_order=""        #creates empty string
    
    for i in range(0,l):    #for loop running legnth of name
        name_order = name_order+list[i] #adds list i to empty string
    
    return(name_order)

def func_14(first, middle, last, title): 
    """
    makes initials of name
    Args:
        first name as a string, middle name list, last name string, title
    Returns:
        initials
    """
    initials = ""               #sets initials = to empty string
    if len(title) > 0:          #if len of title is > 0
        initials = title        #sets the title to the initials
        initials += " "         #adds a space to initials
    initials += first[0]        #adds first letter of first name to 
    
    if len(middle) > 0:         #if len of middle names is > 0
        for i in middle:        #for loop for each element of middle list
            initials += i[0]    #adds first letter to initials
    
    if len(last) > 0:           #if there is a last name
        initials += last[0]     #adds first letter to initials
    
    return initials             #returns initials string


def func_15(title):  
    """
    makes name in alphabetical order
    Args:
        title as string
    Returns:
        boolean (true of false)
    """
    if len(title) == 0:             #if len of title is equal to 0
        return False                #returns false
    else:                           #else
        return True                 #returns true


title, first, middle, last = name_find(name_list, name_titles)  #sets variables equal to what is returned in name_find


while True:             #loop
    func_question = input('''WHAT FUNCTION WOULD YOU LIKE TO DO?
    1. Reverse and display
    2. Vowel frequency
    3. Consonant frequency
    4. Return first name.
    5. Return last name.
    6. Return middle name(s)
    7. Return true or false if last name contains a hyphen
    8. Convert to lowercase
    9. Convert to uppercase
    10. Modify array to create a random name (mix up letters)
    11. Return true or false if first name is a palindrome
    12. Return full-name as a sorted array of characters 
    13. Make initials from name
    14. Return true or false if name contains a title/distinction (“Dr.”, “Sir”, “Esq”, “Ph.d”)
''')    #creates menu to see what func user wants to do and stores the input
    
    if func_question == "1":        #if user inputs "1"
        print(func_1(name))             #runs the function
        play_again = input("Would you like to a different function? (Yes or No:  )")    #asks user to play again?
        if play_again == "yes":     #if user says yes
            continue                #completes the loop again
        else:                       #else
            break                   #breaks loop

    elif func_question == "2":        #if user inputs "2"
        print(func_2(name))             #runs the function
        play_again = input("Would you like to a different function? (Yes or No:  )")    #asks user to play again?
        if play_again == "yes":     #if user says yes
            continue                #completes the loop again
        else:                       #else
            break                   #breaks loop

    elif func_question == "3":        #if user inputs "3"
        print(func_3(name))             #runs the function
        play_again = input("Would you like to a different function? (Yes or No:  )")    #asks user to play again?
        if play_again == "yes":     #if user says yes
            continue                #completes the loop again
        else:                       #else
            break                   #breaks loop

    elif func_question == "4":        #if user inputs "4"
        print(func_4(first))             #runs the function
        play_again = input("Would you like to a different function? (Yes or No:  )")    #asks user to play again?
        if play_again == "yes":     #if user says yes
            continue                #completes the loop again
        else:                       #else
            break                   #breaks loop

    elif func_question == "5":        #if user inputs "5"
        print(func_5(last))             #runs the function
        play_again = input("Would you like to a different function? (Yes or No:  )")    #asks user to play again?
        if play_again == "yes":     #if user says yes
            continue                #completes the loop again
        else:                       #else
            break                   #breaks loop

    elif func_question == "6":        #if user inputs "6"
        print(func_6(middle))             #runs the function
        play_again = input("Would you like to a different function? (Yes or No:  )")    #asks user to play again?
        if play_again == "yes":     #if user says yes
            continue                #completes the loop again
        else:                       #else
            break                   #breaks loop

    elif func_question == "7":        #if user inputs "7"
        print(func_7(last))             #runs the function
        play_again = input("Would you like to a different function? (Yes or No:  )")    #asks user to play again?
        if play_again == "yes":     #if user says yes
            continue                #completes the loop again
        else:                       #else
            break                   #breaks loop

    elif func_question == "8":        #if user inputs "8"
        print(func_8(name, alpha_cap, alpha))             #runs the function
        play_again = input("Would you like to a different function? (Yes or No:  )")    #asks user to play again?
        if play_again == "yes":     #if user says yes
            continue                #completes the loop again
        else:                       #else
            break                   #breaks loop

    elif func_question == "9":        #if user inputs "9"
        print(func_9(name, alpha_cap, alpha))             #runs the function
        play_again = input("Would you like to a different function? (Yes or No:  )")    #asks user to play again?
        if play_again == "yes":     #if user says yes
            continue                #completes the loop again
        else:                       #else
            break                   #breaks loop

    elif func_question == "10":        #if user inputs "10"
        print(func_10(name, alpha_cap, alpha))             #runs the function
        play_again = input("Would you like to a different function? (Yes or No:  )")    #asks user to play again?
        if play_again == "yes":     #if user says yes
            continue                #completes the loop again
        else:                       #else
            break                   #breaks loop

    elif func_question == "11":        #if user inputs "11"
        print(func_11(first))             #runs the function
        play_again = input("Would you like to a different function? (Yes or No:  )")    #asks user to play again?
        if play_again == "yes":     #if user says yes
            continue                #completes the loop again
        else:                       #else
            break                   #breaks loop

    elif func_question == "12":        #if user inputs "12"
        print(func_12(name))               #runs the function
        play_again = input("Would you like to a different function? (Yes or No:  )")    #asks user to play again?
        if play_again == "yes":     #if user says yes
            continue                #completes the loop again
        else:                       #else
            break                   #breaks loop

    elif func_question == "13":        #if user inputs "13"
        print(func_14(first, middle, last, title))             #runs the function
        play_again = input("Would you like to a different function? (Yes or No:  )")    #asks user to play again?
        if play_again == "yes":     #if user says yes
            continue                #completes the loop again
        else:                       #else
            break                   #breaks loop     

    elif func_question == "14":        #if user inputs "14"
        print(func_15(title))             #runs the function
        play_again = input("Would you like to a different function? (Yes or No:  )")    #asks user to play again?
        if play_again == "yes":     #if user says yes
            continue                #completes the loop again
        else:                       #else
            break                   #breaks loop

    else:                                               #else
        print("There are only 14 functions! (1-14)")    #tells user than there are only 14 functions
