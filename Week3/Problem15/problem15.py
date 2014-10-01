__author__ = 'hs0490'
import math

class Problem15:

    def getLogValues(self, fileName):
        contentlist = open(fileName).read().splitlines()
        dnaString = contentlist[0]
        #array A containing at most 20 numbers between 0 and 1
        A = contentlist[1].split(" ")
        #array B having the same length as A in which B[k] represents the common logarithm of the probability
        B = []
        for index in range(0, len(A)):
            gcContent = (float(A[index]))/2
            atContent = (1 - float(A[index]))/2
            atCount = dnaString.count("A")+dnaString.count("T")
            cgCount = dnaString.count("C")+dnaString.count("G")
            totalProduct = math.pow(atContent, atCount) * math.pow(gcContent, cgCount)
            value = math.log10(totalProduct)
            B.append(value)

        return B

    @staticmethod
    def main(self):
        B = Problem15().getLogValues(self)
        for value in B:
            print value,

Problem15.main("problem15.txt")








