#List all natural numbers below 10 that are multiples of 3 or 5.
#We get 3,5,6, and 9.
#The sum of these multiples is 23.
#Find the sum of the multiples of 3 or 5 below 1000. 
#Answer: 233168

count = 1000
result = sum(x for x in range(1, count) if x % 3 == 0 or x % 5 == 0)
print(result)