from usefulStuff import primeFactors
import functools, operator

rad = []
for i in range(2,100001):
    rad += [(functools.reduce(operator.mul, primeFactors(i)),i)]

rad.sort()
print(rad[9998][1])
