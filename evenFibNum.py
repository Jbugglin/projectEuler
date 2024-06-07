#Each new term of Fib sequence = adding previous 2 terms.
# starting at 1 and 2; first 10 are 1,2,3,5,8,13,21,34,55,89.
#Values do not exceed 4M, find sum of even-valued terms. 
#a = a + b
#b = b + a

#Answer: 4613732

a = 0
b = 1
result = 110
sum_list = []
for x in range (result): 
    a = a + b
    if a % 2 == 0 and a < 4000000:
        sum_list.append(a)
    b = a + b
    if b % 2 == 0 and b < 4000000:
        sum_list.append(b)

print(sum(sum_list))