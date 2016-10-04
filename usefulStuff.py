import functools, collections, operator

LIMIT = 1000000

class BoundedOrderedDict(collections.OrderedDict):
    def __init__(self, *args, **kwds):
        self.maxlen = kwds.pop("maxlen", None)
        collections.OrderedDict.__init__(self, *args, **kwds)
        self._checklen()

    def __setitem__(self, key, value):
        collections.OrderedDict.__setitem__(self, key, value)
        self._checklen()

    def _checklen(self):
        if self.maxlen is not None:
            while len(self) > self.maxlen:
                self.popitem(last=False)

def memoize(func=None, maxlen=None):
    if func:
        cache = BoundedOrderedDict(maxlen=maxlen)
        @functools.wraps(func)
        def memo_target(*args):
            lookup_value = args
            if lookup_value not in cache:
                cache[lookup_value] = func(*args)
            return cache[lookup_value]
        return memo_target
    else:
        def memoize_factory(func):
            return memoize(func, maxlen=maxlen)
        return memoize_factory

def genPrimes(n):
    def sieve(n):
        primes = [False,True]*(n//2)
        primes[1] = False
        for (i, checked) in enumerate(primes):
            if checked:
                yield i
                for x in range(i*i,n,2*i):
                    primes[x] = False
    return [2] + list(sieve(n))




def primeFactors(n):
    if n <= 1:
        return []
    for p in _known_primes:
        if n % p == 0: break
    while n % p == 0:
        n //= p
    return [p] + primeFactors(n)

def primeFactorsMulti(n):
    if n <= 1:
        return []
    t = []
    for p in _known_primes:
        if n % p == 0: break
    while n % p == 0:
        t += [p]
        n //= p
    return t + primeFactors(n)

    

def flatten(l):
  return [item for sublist in l for item in sublist]

@memoize
def factorial(n):
  if n < 2: return 1
  else: return n * factorial(n - 1)

def pythagTriples(r):
  if r % 2 == 1:
    return []
  base = (r**2)/2
  d = divisorPairs(base)
  return [(r+s, r+t, r+s+t) for (s,t) in d]

def nCr(n, r):
    r = min(r, n-r)
    if r == 0: return 1
    n = functools.reduce(operator.mul, range(n, n-r, -1))
    d = functools.reduce(operator.mul, range(1, r+1))
    return n//d

def _try_composite(a, d, n, s):
    if pow(a, d, n) == 1:
        return False
    for i in range(s):
        if pow(a, 2**i * d, n) == n-1:
            return False
    return True

_known_primes = genPrimes(LIMIT)
 
def is_prime(n, _precision_for_huge_n=16):
    if n in _known_primes or n in (0, 1):
        return True
    if any((n % p) == 0 for p in _known_primes):
        return False
    d, s = n - 1, 0
    while not d % 2:
        d, s = d >> 1, s + 1
    if n < 1373653:
        return not any(_try_composite(a, d, n, s) for a in (2, 3))
    if n < 25326001:
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5))
    if n < 118670087467:
        if n == 3215031751:
            return False
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7))
    if n < 2152302898747:
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7, 11))
    if n < 3474749660383:
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7, 11, 13))
    if n < 341550071728321:
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7, 11, 13, 17))
    return not any(_try_composite(a, d, n, s))

def powerset(l):
    if not l: return [[]]
    return powerset(l[1:]) + [[l[0]] + x for x in powerset(l[1:])]

@memoize
def fib(n):
    if n in [0,1]: return n
    return fib(n-1)+fib(n-2)

def totient(n):
    if is_prime(n): return n-1
    return n * functools.reduce(operator.mul, [1 - 1/p for p in primeFactors(n)])





