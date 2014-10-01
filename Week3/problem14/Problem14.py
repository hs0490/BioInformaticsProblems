__author__ = 'hs0490'

class Node:

    def __init__(self, number, char, parentNode):
        self.__number = number
        self.__char = char
        if parentNode == "Null":
            self.__parentNode = 0
        else:
            self.__parentNode = parentNode.__number
        self.__adjList = []


    @staticmethod
    def allEdge():
        number = 2
        while number <= len(Trie._trieDict):
            node = Trie._trieDict[number]
            print node.__parentNode,
            print node.__number,
            print node.__char
            number += 1

    def hasEdge(self, char):
        for count in self.__adjList:
            node = Trie._trieDict.get(count)
            if node.__char == char:
                return True
        return False

    def getEdge(self, char):
        for count in self.__adjList:
            node = Trie._trieDict.get(count)
            if node.__char == char:
                return node
        return None

    def addEdge(self, number):
        self.__adjList.append(number)

class Trie:
    _trieDict = {}

    def buildTrie(self, fileName,):
        rootNode = Node(1, "Root", "Null")
        Trie._trieDict[1] = rootNode
        fileobj = open(fileName)
        string = fileobj.readline().replace('\n', '')
        number = 2
        while string:
            parentNode = rootNode
            for char in string:
                if parentNode.hasEdge(char) is False:
                    newNode = Node(number, char, parentNode)
                    Trie._trieDict[number] = newNode
                    parentNode.addEdge(number)
                    parentNode = newNode
                    number += 1
                else:
                    parentNode = parentNode.getEdge(char)

            string = fileobj.readline().replace('\n', '')

class AdjacencyList:

    @staticmethod
    def main(fileName):
        obj = Trie()
        obj.buildTrie(fileName)
        Node.allEdge()


AdjacencyList.main("problem14.txt")


