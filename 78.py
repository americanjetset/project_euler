from usefulStuff import memoize

@memoize
def p(n):
    if n == 0 or n == 1:
        return 1
    else:
        return sum([(-1)**(k+1)*(p(n - k*(3*k - 1)/2) + p(n - k*(3*k + 1)/2)) for k in range(1,int(n+1))])


i = 1
while p(i) % 1000000 != 0:
    i += 1

print(i)
