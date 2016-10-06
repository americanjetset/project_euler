from usefulStuff import primeFactorsMulti
from functools import reduce
from operator import mul

def numSols(n):
    pf = primeFactorsMulti(n)
    return (reduce(mul, [2*b + 1 for (a,b) in pf])+1)/2

n = 100
while True:
    if numSols(n) > 1000:
        print(n)
        break
    n += 1
