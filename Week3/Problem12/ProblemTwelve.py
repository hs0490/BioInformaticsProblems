class ProblemTwelve():

    def __init__(self, n, k):
        self.n = n
        self.k = k
    def rabitcount(self, n):
        if n == 1 or n == 2:
            return 1
        return self.rabitcount(n-1) + self.rabitcount(n-2)*self.k


# n --> months = 32
# k --> pairs = 4

obj = ProblemTwelve(32, 4)
print obj.rabitcount(obj.n)

