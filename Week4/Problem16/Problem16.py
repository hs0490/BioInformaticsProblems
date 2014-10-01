__author__ = 'hs0490'

class Problem16:

    def findLocations(self):
        contentlist = open(self).read().splitlines()
        t = contentlist[0]
        s = contentlist[1]
        for index in range(0, len(t)-len(s)+1):
            seq = t[index:index+len(s)]
            if s == seq:
                print index + 1,


    if __name__ == '__main__':
        findLocations("Problem16.txt")





