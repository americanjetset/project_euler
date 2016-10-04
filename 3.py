from usefulStuff import genPrimes

p = 600851475143

l = 0

for i in genPrimes(int(p**0.5)):
  if p % i == 0:
    l = i

print(i)
