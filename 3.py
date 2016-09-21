from usefulStuff import genPrimes

p = 600851475143
f= []
for i in genPrimes(int(p**0.5)):
  if p % i == 0:
    f += [i]

print(f[len(f)-1])
