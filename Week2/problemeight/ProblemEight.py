__author__ = 'hs0490'
class ProblemEight:

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


    def getProteinString(filename, codontable):
        proteinstring = ""
        rnastring = open(filename).read()
        for index in range(0, len(rnastring), 3):
            seq = rnastring[index: index + 3]
            char = codontable.get(seq)
            if char == 'Stop':
                return proteinstring
            proteinstring += char

        return proteinstring


    codontable = makecodonTable("codontable.txt")
    print getProteinString("rnastring.txt", codontable)












