# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

def gcd(x, y):
    if not y:
        return x
    else:
        return(gcd(y, x % y))

def lcm(x, y):
    return x * y // gcd(x,y)

prod = 1
for i in xrange(1,11):
    for j in xrange(1, i):
        prod *= lcm(i, j)
print lcm()
