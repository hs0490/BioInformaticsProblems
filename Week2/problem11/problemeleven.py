import itertools

__author__ = 'hs0490'

def getComposition(self):
    content = open(self).read()
    dnastring = content.replace("\n", "")
    temp = sorted(set(dnastring))
    for i in itertools.product(temp, repeat=4):
        seq = ''.join(i)
        count = getCount(seq, dnastring)
        print count,



def getCount(seq, dnastring):
    start = 0
    end = 4
    count = 0
    while end <= len(dnastring):
        newseq = dnastring[start: end]
        if seq == newseq:
            count += 1
        start += 1
        end += 1

    return count


getComposition("problem11.txt")


