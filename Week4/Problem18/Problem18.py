__author__ = 'hs0490'

class Problem18:

    def findSharedMotif(self, fileName):
        contentlist = open(fileName).read().split(">Rosalind_")
        stringList = []
        for index in range(1, len(contentlist)):
            string = contentlist[index].splitlines()
            stringList.append("".join(string[1: len(string)]))


        print self.getCommonString(stringList)


    def getCommonString(self, stringList):
        substring = ''
        if len(stringList) > 1 and len(stringList[0]) > 0:
            for index in range(len(stringList[0])):
                for j in range(len(stringList[0])-index+1):
                    if j > len(substring) and all(stringList[0][index:index+j] in x for x in stringList):
                        substring = stringList[0][index:index+j]
            return substring


if __name__ == '__main__':

    obj = Problem18()
    obj.findSharedMotif("Problem18.txt")