__author__ = 'hs0490'
n=5
m=3
generations = [1, 1] #Seed the sequence with the 1 pair, then in their reproductive month.
def fib(i, j):
    count = 2
    while (count < i):
        if (count < j):
            generations.append(generations[-2] + generations[-1]) #recurrence relation before rabbits start dying (simply fib seq Fn = Fn-2 + Fn-1)
        elif (count == j or count == j+1):
            generations.append((generations[-2] + generations[-1]) - 1)#Fn = Fn-2 + Fn-1 - 1
        else:
            generations.append((generations[-2] + generations[-1]) - (generations[-(j+1)])) #Our recurrence relation here is Fn-2 + Fn-1 - Fn-(j+1)
        count += 1
    return (generations[-1])


print (fib(n, m))
print ("Here's how the total population looks by generation: \n" + str(generations))