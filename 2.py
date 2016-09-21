from usefulStuff import memoize

@memoize
def fib(n):
  if n in [1,2]: return n
  else: return fib(n-2) + fib(n-1)

num = 2
s = 0
while fib(num) < 4000000:
  s += fib(num)
  num+=3

print(s)
