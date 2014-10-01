solutionlist = []

def makecodonTable(filename):
    condontable = {}
    content = open(filename).read()
    list = content.splitlines()
    for line in list:
        linelist = line.split(" ")
        index = 0
        while index < len(linelist):
            condontable[linelist[index]] = linelist[index + 1]
            if linelist[index + 1] == 'Stop':
                index += 4
            else:
                index += 7
    return condontable

def findReverseComplement(dnastring):
    newstring = ''
    index = len(dnastring)-1
    while index >= 0:
        char = dnastring[index]
        if char == 'A':
            newchar = 'T'
        elif char == 'T':
            newchar = 'A'
        elif char == 'C':
            newchar = 'G'
        elif char == 'G':
            newchar = 'C'

        newstring += newchar
        index -= 1

    return newstring


def proteinstring(string):
    rnastring = getRNAString(string)
    for index1 in range(0, 3):
        framelist = []
        start = index1
        end = start + 3
        while (start + 3) < len(rnastring):
            framelist.append(rnastring[start: end])
            start += 3
            end = start + 3

        rnaconversion(framelist)

def getRNAString(string):
    rnastring = ''
    for char in string:
        if char == 'T':
            rnastring += 'U'
        else:
            rnastring += char
    return rnastring


def rnaconversion(framelist):
    codontable = makecodonTable("codontable.txt")
    startindex = -1
    endindex = -1
    for index1 in range(0, len(framelist)):
        seq = framelist[index1]
        if seq == "AUG" and startindex == -1:
                startindex = index1
        if codontable.get(seq) == "Stop" and endindex == -1 and startindex != -1:
                endindex = index1
        if startindex != -1 & endindex != -1:
            break

    if startindex < endindex and startindex != -1:
        string = ""
        for index2 in range(startindex, endindex):
            seq = framelist[index2]
            string += codontable.get(seq)
        solutionlist.append(string)



def start(self):
    content = open(self).read()
    contentlist = content.splitlines()

    for content in contentlist:
        proteinstring(content)
        proteinstring(findReverseComplement(content))
        solutionlist.reverse()
        for string in solutionlist:
            print string


start("problemnine.txt")
