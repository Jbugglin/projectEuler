import math
# n! means: n x (n - 1) x ... x 3 x 2 x 1
# Example: 10! = 10 x 9 x ... x 3 x 2 x 1 = 3628800
# The sum of the digits in 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27
# Find the sum of digits in 100!

# Answer: 648
factoral_value = 100
factorial_answer = math.factorial(factoral_value)
#print("The factorial of" ,factoral_value, "is", factorial_answer)

def getDigitSum(n):
    sum = 0 
    for digit in str(n):
        sum += int(digit)
    return sum
n = factorial_answer
print("The factorial digit sum is:" ,getDigitSum(n))