#The prime factors of 13195 are 5, 7, 13, and 29.
#Find the largest prime factor of 600851475143
#71 x 839 x 1471 x 6857

#Answer: 6857...largest prime.

startingNumber = 600851475143
divisibleNumbers = 0
for x in range(1, startingNumber):
    if startingNumber % x == 0:
        divisibleNumbers = x
        for x in range(1, divisibleNumbers):
            if divisibleNumbers % x == 0:
                print(x)