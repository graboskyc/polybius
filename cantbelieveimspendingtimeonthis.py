import collections

ClearText = collections.namedtuple("ClearText", ["String","Number"])

# given a character, convert to the numeric form (a->1, b->2, etc)
# based on ascii table
def convertToOrd(char):
    return str(ord(char.lower()) - 96)

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
            retNum.append(convertToOrd(char).ljust(2))
        i = i + 1
    r = ClearText(retStr, retNum)
    
    print " ".join(r.String)
    print " ".join(r.Number)
    print "\r\nREVERSED\r\n"
    print " ".join(reversed(r.String))
    print " ".join(reversed(r.Number))

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

text = """This game had a very limited release, one or two backwater arcades in a suburb of Portland. The history of this game is cloudy, there were all kinds of strange stories about how kids who played it got amnesia afterwards, couldn't remember their name or where they lived, etc.
The bizarre rumors about this game are that it was supposedly developed by some kind of weird military tech offshoot group, used some kind of proprietary behavior modification algorithms developed for the CIA or something, kids who played it woke up at night screaming, having horrible nightmares.

According to an operator who ran an arcade with one of these games, guys in black coats would come to collect "records" from the machines. They're not interested in quarters or anything, they just collected information about how the game was played.

The game was weird looking, kind of abstract, fast action with some puzzle elements, the kids who played it stopped playing games entirely, one of them became a big anti videogame crusader or something. We've contacted one person who met him, and he claims the machines disappeard after a month or so and no one ever heard about them again."""

# basic offsets to start
offsetList = (16, 10, 5)

# iterate over each offset
for offset in offsetList:
    printHead("Using Offset of: " + str(offset), False)

    printHead("Original String")
    printEvery(text, offset)
    print "\r\n\r\n"

    printHead("Cutting whitespace")
    cleanText = ''.join(text.split())
    printEvery(cleanText, offset)
    print "\r\n\r\n"

    printHead("Removing commas")
    replaceList = (",")
    cleanText = replaceStr(cleanText, replaceList)
    printEvery(cleanText, offset)
    print "\r\n\r\n"

    printHead("Removing periods")
    replaceList = (".")
    cleanText = replaceStr(cleanText, replaceList)
    printEvery(cleanText, offset)
    print "\r\n\r\n"

    printHead("Removing quotes")
    replaceList = ("'", "\"")
    cleanText = replaceStr(cleanText, replaceList)
    printEvery(cleanText, offset)
    print "\r\n\r\n"

    printHead("Removing colons")
    replaceList = (":",";")
    cleanText = replaceStr(cleanText, replaceList)
    printEvery(cleanText, offset)
    print "\r\n\r\n"