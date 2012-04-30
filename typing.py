import random
import time
    

def menu():
    prompt = " P)play\n"
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
            if c=='p':
                play()
            elif (c=='r') or (c=='R'):
                rules()
                c='q'

def userChoice(prompt, c):
    """prompt - a string containing the prompt to display.
       c - a tuple containing list of valid input choices."""
    userInput = raw_input(prompt)
    while (userInput not in c):
        print prompt
        userInput = raw_input(prompt)
    return userInput

def makelist():
    liopen = open("words.txt")
    theList = []
    for entry in liopen:
        entry = entry.strip()
        theList.append(entry)
    liopen.close()
    return theList

def randomword(theList):
    return random.choice(theList)


def play():
    usedtime = 0.0
    remtime = 0.0
    twords = 0
    cwords = 0
    listi = makelist()
    while (usedtime <= 5):
        word = randomword(listi)
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
    print "Number of words typed:", twords
    print "Number of misspelled words:", twords - cwords
    print "RAW words per minute:", (twords/usedtime) * 100.0, "wpm"
    actual=(cwords/usedtime) * 100.0
    print "Actual words per minute:",actual, "wpm"
    scores=scorelist()
    addscore(scores,actual)
    writescore(scores)

## --------------------------------------------------------##
## HIGHSCORE FUNCTIONS!

def scorelist():
    try:
        fout = open("highscore.csv", "r")
        scores=[]
        for record in fout:
            record=record.strip()
            scores.append(record)
        fout.close()
        print "no error", scores
        return scores
    except IOError as e:
        print " :(( error"
        return []
        
def bubbleSort(theList):
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
    if eligible(theList, score):
        print "Congrats! You made the top 10."
        name = raw_input("What is your name: ")
        entry=(name, score)
        theList.append(entry)
        bubbleSort(theList)
        if len(theList)>10:
            #only keep top 10 values
            theList.pop()
    else:
        print "BOOOOOOOO!"

def writescore(theList):
    fout = open("highscore.csv", "w")
    bubbleSort(theList)
    for entry in theList:
        csvData = entry[0]+","+str(entry[1])+"\n"
        fout.write(csvData)
    fout.close()
    
