import functools, collections

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
    primes = [True] * n
    primes[0] = primes[1] = False
    for i in range(2,n,2):
      primes[i] = False
    for (i, check) in enumerate(primes):
      if check:
        yield i
        for x in range(i*i,n,2*i):
          primes[x] = False
  return [2] + list(sieve(n))

@memoize
def primeFactors(n):
  factors = []
  n1 = n
  pList = genPrimes(n+1)
  for i in pList:
    if n % i == 0:
      n1 = n1 / i
      factors += [i]
  if n1 == 1:
    return factors
  else:
    return factors + primeFactors(n1)

def divisorPairs(n):
  div = []
  for d in range(1,int(n**0.5)+1):
    if n % d == 0:
      div += [(d,n/d)]
  return div

def divisors(n):
  div = []
  for d in range(1,int(n**0.5)+1):
    if n % d == 0:
      div += [d,n/d]
  return list(set(div))

def flatten(l):
  return [item for sublist in l for item in sublist]

@memoize
def factorial(n):
  if n == 1: return 1
  else: return n * factorial(n - 1)

def pythagTriples(r):
  if r % 2 == 1:
    return []
  base = (r**2)/2
  d = divisorPairs(base)
  return [(r+s, r+t, r+s+t) for (s,t) in d]













  

