import random
import time

def userChoice(prompt, c):
    """prompt - a string containing the prompt to display.
       c - a tuple containing list of valid input choices."""
    userInput = raw_input(prompt)
    while (userInput not in c):
        print prompt
        userInput = raw_input(prompt)
    return userInput

def makelist():
    """makes the list of words from words.txt file"""
    liopen = open("words.txt")
    theList = []
    for entry in liopen:
        entry = entry.strip()
        theList.append(entry)
    liopen.close()
    return theList

def randomword(theList):
    """chooses a random word from the wordlist"""
    return random.choice(theList)

def rules():
    """Rules of the game"""
    print "Welcome"
    print "Test your typing skills..."
    print "Type as many words as you can in under 60 seconds and get your RAW words per minute and actual words per minute"

def play():
    """Play function of the game."""
    usedtime = 0.0
    remtime = 0.0
    twords = 0
    cwords = 0
    listi = makelist()
    while (usedtime <= 60):
        word = randomword(listi)
        listi.remove(word)
        remtime = 60.0 - usedtime
        print remtime
        print word
        start = time.clock()
        inp = raw_input("Enter a word:")
        end = time.clock()
        if (inp == word):
            cwords += 1
        usedtime += (end - start)
        twords += 1
    print "TIMES UP!"
    print "Total no. of words:", twords
    incwords=twords - cwords
    print "No. of incorrect words", incwords
    raw=(twords/usedtime) * 60.0
    print "RAW words per minute %.2f" %raw
    actual=(cwords/usedtime) * 60.0
    print "Actual words per minute: %.2f"%actual
    scores=scorelist()
    addscore(scores,actual)
    writescore(scores)

def menu():
    """Menu for the game"""
    prompt = "P)lay\n"
    prompt = prompt + "R)ules of the game\n"
    prompt = prompt + "D)isplay high scores\n"
    prompt = prompt + "Q)uit\n"
    prompt = prompt + "Please choose one:"
    choices = ("P", "p", "R", "r", "D", "d", "Q", "q")
    c = userChoice(prompt, choices)
    if c=='q' or c=='Q':
            print "You quit..."
    else:
        while c!='q' or c!='Q':
            if (c=='p') or (c=='P'):
                play()
                c='q'
            elif (c=='r') or (c=='R'):
                rules()
                c='q'

## --------------------------------------------------------##
## HIGHSCORE FUNCTIONS!

def scorelist():
    """returns the list of scores"""
    scores=[]
    try:
        fout = open("highscore.csv", "r")    
        for entry in fout:
            entry=entry.strip()
            entrie=entry.split(",")
            record=(entrie[0], entrie[1])
            scores.append(record)
        fout.close()
        return scores
    except IOError as e:
        return scores
        
def bubbleSort(theList):
    """Bubblesorts the list"""
    lastIndex = len(theList)-2
    while lastIndex >= 0:
        i = 0
        while i <= lastIndex:
            if theList[i][1] < theList[i+1][1]:
                theList[i], theList[i + 1] = theList[i + 1], theList[i]
            i +=1
        lastIndex -= 1


def eligible(theList,score):
    """Returns True if the score is to be added to the list, otherwise False"""
    bubbleSort(theList)
    if len(theList) < 10:
        return True
    else:
        if score > theList[-1][1]: #the value of the last score in the list.
            return True
    return False # score is not eligible

def addscore(theList, score):
    """adds the eligible score to theList"""
    if eligible(theList, score):
        print "Congrats! You made the top 10."
        name = raw_input("What is your name: ")
        entry=(name, score)
        theList.append(entry)
        bubbleSort(theList)
        print theList

        if len(theList)>10:
            #only keep top 10 values
            theList.pop()
        return theList
    else:
        print "BOOOOOOOO!"
        return theList

def writescore(theList):
    """writes the scores present in theList to the file"""
    fout = open("highscore.csv", "w")
    bubbleSort(theList)
    for entry in theList:
        record= entry[0]+","+str(entry[1])+"\n"
        fout.write(record)
    fout.close()
