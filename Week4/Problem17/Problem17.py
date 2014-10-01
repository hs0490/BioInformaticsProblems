import urllib

__author__ = 'hs0490'

class Problem17:

    def findLocations(self, fileName):
        fileObj = open(fileName)
        # id --> Protein Database access ID
        id = fileObj.readline().replace('\n', '')

        while id != "":
            # t ---> string from Protein Database access ID
            t = ''.join(self.getString2(id))

            # list storing index at which substring is found
            indexlist = []
            for index in range(0, len(t) - 3):
                seq = t[index: index + 4]
                if self.checkString(seq) is True:
                    indexlist.append(index+1)

            if len(indexlist) != 0:
                print "\n"+id
                for index in indexlist:
                    print index,

            id = fileObj.readline().replace('\n', '')


    # returns string from Protein Database access ID
    def getString2(self, id):
        link = "http://www.uniprot.org/uniprot/"+id+".fasta"
        string = urllib.urlopen(link).read().splitlines()
        return string[1:len(string)]

    # return true if string matches the condition N{P}[ST]{P}
    def checkString(self, string):
        if string[0] == 'N' and string[1] != 'P' and string[3] != 'P':
            if string[2] == 'S' or string[2] == 'T':
                return True


if __name__ == '__main__':
    obj = Problem17()
    obj.findLocations("Problem17.txt")
