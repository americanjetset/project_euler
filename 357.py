from usefulStuff import genPrimes as primes

p = primes(100000000)
d = []

possible = [i-1 for i in p if (i-1) % 4 != 0]

print(len(possible))

for i in possible:
    if i == 6:
        pass
    else:
        if i % 10 == 6:
            possible.remove(i)

def con2(n):
    if int(2 + n/2) in p: return True
    else: return False

def con3(n):
    for d in range(3,int(n**0.5)):
        if n % d == 0:
            if int(d + n/d) not in p:
                return False
    return True

print(len(possible))


