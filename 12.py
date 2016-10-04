from usefulStuff import *

@memoize
def triangle(n):
  if n == 1: return 1
  else: return triangle(n-1) + n

def func12():
  i = 1
  while len(divisors(triangle(i))) < 501:
    i += 1
  return triangle(i)



func12()