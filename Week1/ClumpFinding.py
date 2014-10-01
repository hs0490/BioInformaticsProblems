__author__ = 'hs0490'
class ClumpFinding:

    def findclump(filename):
        content = open(filename).read()
        list = content.splitlines()
        genomestring = list[0]
        list2 = list[1].split(" ")
        k = int(list2[0])
        l = int(list2[1])
        t = int(list2[2])
        patternlist = []
        for index in range(0, len(genomestring)):
            testString = genomestring[index:index+k]
            count = 1
            for index2 in range(index+k, l+index):
                if genomestring[index2:index2+k] == testString:
                    count += 1
            if count == t:
                patternlist.append(testString)

        for pattern in patternlist:
            print pattern,

    findclump("sample2.txt")





