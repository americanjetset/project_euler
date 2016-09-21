# x^2 - D*y^2 = 1
#
#
# TAKES FOREVER
#
#





from math import sqrt
from fractions import Fraction
from decimal import *

getcontext().prec = 6000

def contfrac(r,depth):

  if depth == 1:
    return [int(r)]

  i = int(r)

  f = r - i

  return [i] + contfrac(Decimal(1)/f,depth-1)



def convergents(D,depth=1):

  l = contfrac(Decimal(D).sqrt(),depth)

  p = l.pop()

  l = l[::-1]

  for i in l:

    p = i + Fraction(1,p)

  return p


def isSolution(x,y,D):

  if x**2 - D*(y**2) == 1:
    return True
  return False


def func66(i):

  if sqrt(i).is_integer():
    return 0
  else:

    d = 1

    x = convergents(i,d).numerator
    y = convergents(i,d).denominator

    while not isSolution(x,y,i):
      d += 1
      x = convergents(i,d).numerator
      y = convergents(i,d).denominator
    return x


m = [0,0]

for i in range(2,1000):

  if func66(i) > m[0]:
    m = [func66(i),i]

m
