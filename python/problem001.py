# Find the sum of all the multiples of 3 or 5 below 1000.

def findSumMultiples(x1, x2, upper):
    total = 0 ;
    for i in xrange(1, 1000):
        if (i % x1 == 0 or i % x2 == 0):
            total += i
    return total

print findSumMultiples(3, 5, 1000)
