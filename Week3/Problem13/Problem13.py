__author__ = 'hs0490'

class Problem13:

    def rabitFibonacci(self, months, age):
        rabitGeneration = [1, 1]
        count = 2
        while count < months:
            if count < age:
                rabitGeneration.append(rabitGeneration[-2] + rabitGeneration[-1])
            elif count == age or count == age+1:
                rabitGeneration.append((rabitGeneration[-2] + rabitGeneration[-1]) - 1)
            else:
                rabitGeneration.append((rabitGeneration[-2] + rabitGeneration[-1]) - (rabitGeneration[-(age+1)]))
            count += 1

        return rabitGeneration[-1]



print Problem13().rabitFibonacci(85, 20)