from usefulStuff import memoize

# function p returns the number of total partitions.
# the problem only requires partitions of 2 or more positive integers, so function P removes the single-int representation, i.e. for 100, "100"

@memoize
def p(n):
    n = int(n)
    if n == 0 or n == 1:
        return 1
    else:
        return sum([(-1)**(k+1)*(p(n - k*(3*k - 1)/2) + p(n - k*(3*k + 1)/2)) for k in range(1,n+1)])

def P(n):
    return p(n) - 1
