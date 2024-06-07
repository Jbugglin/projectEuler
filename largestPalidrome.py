#The largest palindrome from product of 2 digit number 9009 = 91 x 99.
#Find the largest palindrome from the product of two 3-digit numbers.
#Answer 906609
product = 0
temp = 0
for x in range(100, 1001):
    for y in range(100, 1001):
        product = x * y
        temp = product
        s = str(temp)
        reverse = s[::-1]
        if(s == reverse):
            print("Pal: " + s)