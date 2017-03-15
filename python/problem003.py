# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143 ?

num = 600851475143
currentDiv = 2

while num != currentDiv:
    if num % currentDiv == 0:
        num /= currentDiv
        currentDiv = 2
        continue
    currentDiv += 1

print num
