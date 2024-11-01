'''
Author: Zac Rosenbaum
Date: 10/30/2024
Description: 
Features: None
Bugs: None
Sources: 
https://stackoverflow.com/questions/16976096/take-the-first-x-elements-of-a-dictionary-on-python

'''
import string                       #brings in string library
import csv                          #brings in csv library
from collections import Counter     #brings in counter library
import sys                          #brings in sys library

trump_speech = "cleaned_trump_speech_transcript.txt"     #sets trump speech to the txt file 
kamala_speech = "kamala_new.txt"                         #sets trump speech to the txt file

"""
    Reads in the txt file makes a dictionary with the words in file and frequency

    Args:
        speech, or the txt file name

    Returns:
       the dictionary of 15 elements in the most common words stated
"""
def read_file(speech):
    f = open(speech)                                           #opens the txt file
    counts = {}                                                #sest counts as an empty dictionary
    for line in f:                                             #for each line in the opened file
        line = line.translate(str.maketrans("", "",
                                    string.punctuation))       #gets rid of all puncutaion from the opened file
        useless_words = ["which", "been", "more", "new", "no", "am", "than", "every", "ever", "or", "can", "its", "these", "make", "other", "also", "most", "any" "never", "going", "has", '\n', "but", "your", "her", "own", "now", "how", "and", "the", "to", "of", "i", "a", "in", "for", "our", "we", "that", "is", "he", "are", "will", "who", "my", "with", "us", "be", "as", "she", "not", "you", "on", "it", "this", "an", "when", "have", "has" "but", "would", "was", "one", "their", "me", "all", "know", "they", "his", "about", "up", "at", "because", "out", "what", "so", "from", "always", "let", "by", "your" "going", "like", "had", "them", "were", "had"]
        #useless words creates a list of a bunch of filler words
        line = line.lower()             #lowers each line of file
        words = line.split(" ")         #splits the lines into words by separating lines by the spaces
        for word in words:              #for loop for each word in each line
            if word in useless_words:   #if the word is inside the useless words lists
                continue                #it doesn't add it to counts, it skips the rest of the list for that word
            elif word not in counts:    #else if the word isnt inside the counts dict
                counts[word] = 1        #add the word to counts dict
            else:                       #else
                counts[word] += 1       #add another vaule/frequency for that word in counts dict
    del counts['']                      #deletes the element that has nothing in it

    output = dict(sorted(counts.items(), key=lambda item: item[1], reverse=True)) #sets output = to counts dict in decending order
    output = dict(Counter(output).most_common(15))      #only takes the 15 most common values
    return(output)                                      #returns the decending,15 element dict
"""
    writes dictionary  into csv

    Args:
        speech, or the dictionary

    Returns:
       csv file
"""   
def csv_write(speech):                                      
    with open('Names.csv', 'w', newline='') as csvfile:                 #opens csv and writes
        writer = csv.writer(csvfile)                                    #sets writer to the csv writer
        for key, value in speech.items():                               #for loop with key and value in dictionary
            if value > 5:                                               # if the value/frequency of the word is more than 5,
                csvfile.writelines(key + "," + str(value) + "\n")       #writes the dictionary to the csv
            else:                                                       #if else
                continue                                                #skips through the loop
            #writer.writerows([key, value])
            

def main():                                     #defines main func
    t_output = read_file(trump_speech)          #runs the first func with trump speech
    k_output = read_file(kamala_speech)         #runs the first func with kamala speech
    ask = str.lower(input("which speech would you like to see? ('Kamala' or 'Trump')")) #asks user to pick which speech to check
    if ask == "kamala":         #if uers says kamala
       csv_write(k_output)      #runs the kamala speech to csv
    elif ask == "trump":        #if uers says trump
       csv_write(t_output)      #runs the trump speech to csv
    else:                       #else
        sys.exit("user must either choose 'Kamala' or 'Trump'") #exits the program

main() #runs main function




