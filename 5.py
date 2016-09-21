from usefulStuff import *

result = 1

multiplicity = []

def maxCount(lis, elem):
  count = 0
  for l in lis:
    count = max(l.count(elem),count)
  return count

for p in genPrimes(20):
  multiplicity += [maxCount([primeFactors(i) for i in range(2,21)],p)]

for (p,m) in zip(genPrimes(20),multiplicity):
  result *= (p**m)

print(result)
