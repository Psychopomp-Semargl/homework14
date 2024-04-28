import math

def test(n, *args, txt):
    s=0
    for i in range(len(args)):
        s += n * args[i]
        print("Число равно:", s)
print(test(1,2,3,4,5, txt = "Число равно:"))

def factorial(n):
    if n == 0:
         return 1
    else:
         return n * factorial(n-1)
print(factorial(5))
