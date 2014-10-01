__author__ = 'hs0490'
class DNAToRNAString:

    def getRNAString(filename):
        fileobject = open(filename)
        dnastring = fileobject.read()
        rnastring = ''
        for char in dnastring:
            if char == 'T':
                rnastring += 'U'
            else:
                rnastring += char
        return rnastring

    print getRNAString("problem7.txt")





