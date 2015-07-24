######### Assignment 4 ##########
######### Navdeep Pal ###########
######### Date : 02/08/2015 #####
######### Chapter 5, Program exercise 14

#  This program analyzes a file to determine the number of lines, words, and characters contained therein.

def wc():
    inFile  = input("Please enter the file name: ")
    inRead = open(inFile, "r")
    inText = inRead.readlines()
    countWord = 0
    inRead.read()
    cLine = 0
    cChar = 0
    for line in inText:
        cLine = cLine+1
        cWord = line.split()
        countWord = len(cWord) + countWord
        cCount = len(line)
        cChar = cCount + cChar
    print("Number of Lines in the file =", cLine, "\n" "Number of Words in the file =", countWord, "\n" "Number of Characters in the file =", cChar)
    inRead.close()
wc()
    
    