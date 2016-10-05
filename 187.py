from usefulStuff import genPrimes

def numSemiprimes(x):
    base = genPrimes(int(x**0.5))
    return sum([len(genPrimes(int(x/base[k-1])+1)) - k + 1 for k in range(1,len(base)+1)])
    
