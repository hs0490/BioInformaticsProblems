# coding=utf-8
import itertools

__author__ = 'hs0490'

class ProblemTenth:

     # Given: A collection of at most 10 symbols defining an ordered alphabet, and a positive integer n (n≤10).
     # Return: All strings of length n that can be formed from the alphabet, ordered lexicographically.


    def getstring(self):
        content = open(self).read()
        contentlist = content.splitlines()
        symbollist = contentlist[0].split()
        length = int(contentlist[1])

        for i in itertools.product(symbollist, repeat=length):
            print ''.join(i)


    getstring("problemten.txt")























    getstring("problemten.txt")

