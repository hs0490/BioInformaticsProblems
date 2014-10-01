__author__ = 'hs0490'

class Problem19:

    def failureArray(self, fileName):
        content = open(fileName).read().splitlines()
        string = "".join(content[1: len(content)])
        index = -1
        array1 = [index]
        for index2, array2 in enumerate(string):
            while index >= 0 and string[index] != array2:
                index = array1[index]
            index += 1
            array1.append(index)
        print ' '.join(map(str, array1[1:]))

if __name__ == "__main__":
    Problem19().failureArray('Problem19.txt')