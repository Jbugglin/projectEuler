#Sum of the squares => 1^2 + 2^2 ... + 10^2 = 385
#square of the sum => (1 + 2 + ... + 10)^2 = 3025
#Difference is: 3025 - 385 = 2640.
#Find difference between sum of squares of first 100 natural numbers and the square of the sum. 

#Sum of the sqares 100.
sumOfSquare = []
sosAns = 0
for x in range(1, 101):
    temp = x * x
    sumOfSquare.append(temp)
    sosAns = sum(sumOfSquare)

#print(sosAns)

#Square of the sum of 100 natural numbers.
squareOfSum = []
sqos = 0
for x in range(1, 101):
    squareOfSum.append(x)
    sqos = sum(squareOfSum)
sqos = sqos * sqos
#print(sqos)

#Difference so square of sum and sum of squares
difference = sqos - sosAns
print(difference)