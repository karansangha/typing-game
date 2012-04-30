# High score prototype
# score filename: highscore.dat
# a CSV text file
# each record is on its on line
# format: name, score

# To do this prototype:
# 1)Put it into a "list of tuples" format
# 2) SOrt the list by the score
# 3) Write back score list as CSV to a file
# 4) Add a "new score" to the list
# 5) Remove unwanted item from the list(top 10)
# 6) Check to see if "new score" is eligible to be entered
# 7) Print out high score list on the screen

def readscore(fname = "highscore.txt"):
    hiscore = []
    fin = open(fname)

    for record in fin:
        record = record.strip() #strips non-printing characters
        data = record.split(",")

        entry = (data[0], int(data[1]))
        # the variable entry is a tuple. We can tell because it is being
        # assigned something within paranthesis
        # data a position at 0 is the "name" - no cats required
        # data at position 1 is the "score" - it needs to be casted as an int
        hiscore.append(entry)
    fin.close()
    return hiscore


def bubbleSort(theList):
    lastIndex = len(theList)-2
    while lastIndex >= 0:
        i = 0
        while i <= lastIndex:
            if theList[i][1] < theList[i][1]:
                theList[i], theList[i + 1] = theList[i + 1], theList[i]
            i +=1
        lastIndex -= 1

def printscore(theList):
    """print the score on the screen"""
    count = 1
    print "Rank\tName\t\tScore"
    print "----\t----\t\t-----"
    for entry in theList:
        print str(count)+"\t"+entry[0]+"\t\t"+str(entry[1])
        count += 1

def newscore(theList, score):
    """Returns True if the score is to be added to the list, otherwise False"""
    bubbleSort(theList)
    if len(theList) < 10:
        return True
    else:
        if score > theList[-1][1]: #the value of the last score in the list.
            return True
    return False # score is not eligible

def addscore(theList, score):
    if newscore(theList, score):
        print "Congrats! You made the top 10."
        name = raw_input("What is your name:")
        entry(name, score)
        theList.append(entry)
        bubbleSort(theList)

        if len(theList)>10:
            #only keep top 10 values
            theList.pop()

def writescore(theList):
    fout = open("highscore.csv", "w")

    for entry in theList:
        csvData = entry[0]+","+str(entry[1])+"\n"
        print csvData
        fout.write(csvData)
    fout.close()

hiscore=readscore()    
slist=bubbleSort(hiscore)
printscore(slist)
