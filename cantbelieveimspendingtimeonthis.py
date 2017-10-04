import collections
import base64

##############################################
# FUNCTIONS
##############################################

ClearText = collections.namedtuple("ClearText", ["String","Number","ModFive", "Poly"])

# given a character, convert to the numeric form (a->1, b->2, etc)
# based on ascii table
def convertCharToOrd(char):
    return str(ord(char.lower()) - 96)

# given a number, convert to alpha form (1-->a, 2-->b, etc)
# based on ascii table
def convertOrdToChar(num):
    return chr(num+96)

def polybiusCoordToString(lr,ud):
    r1 = ['A', 'B', 'C', 'D', 'E']
    r2 = ['F', 'G', 'H', 'I', 'K']
    r3 = ['L', 'M', 'N', 'O', 'P']
    r4 = ['Q', 'R', 'S', 'T', 'U']
    r5 = ['V', 'W', 'X', 'Y', 'Z']
    poly = [r1, r2, r3, r4, r5]

    lr = int(lr)
    ud = int(ud)

    #print str(lr) + " and " + str(ud) + " yields " + poly[ud][lr]

    return poly[ud][lr]

# common print
# used to check the string forwards, back, base 64, mod, etc
def commonPrint(ct):
    # print out the string, the number of letter in alphabet
    # then do the same as above but reverse each
    print "\r\nSTRAIGHT FORWARD\r\n"
    print " ".join(ct.String)
    print " ".join(ct.Number)

    print "\r\nREVERSED\r\n"
    print " ".join(reversed(ct.String))
    print " ".join(reversed(ct.Number))

    # is this a base 64 encoded string?
    print "\r\nBASE64 DECODE\r\n"
    try:
        print base64.b64decode(''.join(ct.String.split()))
    except:
        print "Not valid base64 encoded string"
    
    # maybe its mod5 for a polybius square?
    print "\r\nLETTER INDEX MOD 5\r\n"
    for i in ct.Number:
        ct.ModFive.append(str(int(str(i)) % 5))
    print " ".join(ct.ModFive)
    print "".join(reversed(" ".join(ct.ModFive)))

    print "\r\nVAL FROM POLY SQUARE\r\n"
    firstInPair = True
    v1 = 0
    v2 = 0
    for i in ct.ModFive:
        if firstInPair:
            v1 = i
            firstInPair = False
        else:
            firstInPair = True
            v2 = i
            ct.Poly.append(polybiusCoordToString(int(v1), int(v2)))
    print " ".join(ct.Poly)
    print "".join(reversed(" ".join(ct.Poly)))

#given a full text, find every nth character
def printEvery(text, offset):
    i = 0
    retStr = []
    retNum = []
    for char in text:
        if (i == offset):
            i = 0
        if(i == 0):
            retStr.append(char.ljust(2))
            retNum.append(convertCharToOrd(char).ljust(2))
        i = i + 1
    r = ClearText(retStr, retNum, [], [])
    
    commonPrint(r)
    

# remove certain characters inputted as a list from a string
def replaceStr(text, removeChars):
    retStr = text
    for char in replaceList:
        retStr = retStr.replace(char, "")
    return retStr

# headings
def printHead(heading, indent=True):
    frontchar = ""
    if indent:
        frontchar = "\t\t"
    print frontchar + "+-------------------------------+"
    print frontchar + "|"+heading
    print frontchar + "+-------------------------------+"

##############################################
# Globals
##############################################
# The special text in question
text = """This game had a very limited release, one or two backwater arcades in a suburb of Portland. The history of this game is cloudy, there were all kinds of strange stories about how kids who played it got amnesia afterwards, couldn't remember their name or where they lived, etc.
The bizarre rumors about this game are that it was supposedly developed by some kind of weird military tech offshoot group, used some kind of proprietary behavior modification algorithms developed for the CIA or something, kids who played it woke up at night screaming, having horrible nightmares.

According to an operator who ran an arcade with one of these games, guys in black coats would come to collect "records" from the machines. They're not interested in quarters or anything, they just collected information about how the game was played.

The game was weird looking, kind of abstract, fast action with some puzzle elements, the kids who played it stopped playing games entirely, one of them became a big anti videogame crusader or something. We've contacted one person who met him, and he claims the machines disappeard after a month or so and no one ever heard about them again."""

# Test phrase
#text = "Iaaa aCbb bbant hjn sgjktsdghbyu adepeabl ieii eilgril lq i v ease ei zmv"

##############################################
# TEST ONE:
# check every nth character for a pattern
##############################################
# basic offsets to start (n)
offsetList = (16, 10, 5)

# iterate over each offset
for offset in offsetList:
    printHead("TEST ONE: every nth character\r\n|Using Offset of: " + str(offset), False)

    printHead("Original String, offset " + str(offset))
    printEvery(text, offset)
    print "\r\n\r\n"

    printHead("Cutting whitespace, offset " + str(offset))
    cleanText = ''.join(text.split())
    printEvery(cleanText, offset)
    print "\r\n\r\n"

    printHead("Removing commas, offset " + str(offset))
    replaceList = (",")
    cleanText = replaceStr(cleanText, replaceList)
    printEvery(cleanText, offset)
    print "\r\n\r\n"

    printHead("Removing periods, offset " + str(offset))
    replaceList = (".")
    cleanText = replaceStr(cleanText, replaceList)
    printEvery(cleanText, offset)
    print "\r\n\r\n"

    printHead("Removing quotes, offset " + str(offset))
    replaceList = ("'", "\"")
    cleanText = replaceStr(cleanText, replaceList)
    printEvery(cleanText, offset)
    print "\r\n\r\n"

    printHead("Removing colons, offset " + str(offset))
    replaceList = (":",";")
    cleanText = replaceStr(cleanText, replaceList)
    printEvery(cleanText, offset)
    print "\r\n\r\n"

##############################################
# TEST TWO:
# see if something is partitioned by punctuation
##############################################
# see if theres anything hidden by punctuation partitioning
# convert number of words in a phrase splut by punctuation characters
# and convert that to letter of alphabet
print "\r\n\r\n\r\n\r\n"
printHead("TEST TWO: \r\n|Trying to split on punctuation", False)

splitChars = (",",".","\"","'")
splitText = text
usedChars = ""
for char in splitChars:
    usedChars = usedChars + " " + char
    splitText = splitText.replace(char,"||")
    textArray = splitText.split("||")
    printHead("Splitting on: " + usedChars + " and word counts in each phrase are:")
    ct = ClearText([], [], [], [])
    for phrase in textArray:
        ct.Number.append(str(len(phrase.split(" "))).ljust(2))
        ct.String.append(convertOrdToChar(len(phrase.split(" "))).ljust(2))

    commonPrint(ct)
    print "\r\n\r\n"


##############################################
# TEST Three:
# word length
##############################################
print "\r\n\r\n\r\n\r\n"
printHead("TEST THREE: \r\n|Word length", False)

cleanTextWithSpaces = ""
replaceList = (":",";",",",".","'","\"","?", "(", ")", "!")
cleanTextWithSpaces = replaceStr(text, replaceList)
splitText = cleanTextWithSpaces.strip().split(" ")
ct = ClearText([], [], [], [])
for word in splitText:
    ct.Number.append(str(len(word)).ljust(2))

commonPrint(ct)