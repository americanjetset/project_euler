from usefulStuff import genPrimes,totient
from functools import reduce
from operator import mul
from math import log as ln


def R(n):
    return totient(n)/(n-1)

def primorial(n):
    primes = genPrimes(100)
    return reduce(mul, primes[:n])

test = [primorial(n) for n in range(1,10)]

m = 10**25
for p1 in test:
    for p2 in test:
        for p3 in test:
            if R(p1*p2*p3) < 15499/94744:
                m = min(m,p1*p2*p3)

print(m)
                
        
