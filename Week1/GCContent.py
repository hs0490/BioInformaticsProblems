from __future__ import division
__author__ = 'hs0490'
class GCContent:

    def highestGCContent(filename, ):
        dict = {}
        fileObj = open(filename)
        content = fileObj.read()
        contentlist = content.split('>')
        for index in range(1, len(contentlist)):
            dnastringlist = contentlist[index].splitlines()
            id = dnastringlist[0]
            dnastring = dnastringlist[1]
            for index2 in range(2, len(dnastringlist)):
                dnastring += dnastringlist[index2]
            cgcount = dnastring.count('C') + dnastring.count('G')
            gccontent = (cgcount/len(dnastring))*100
            dict[gccontent] = id
        sorteddict = (sorted(dict))
        maxgccontent = sorteddict[len(sorteddict)-1]
        highestid = dict.get(maxgccontent)
        print highestid
        print round(maxgccontent, 6)

    #highestGCContent("sample.txt")
    highestGCContent("/home/hs0490/Downloads/rosalind_gc.txt")