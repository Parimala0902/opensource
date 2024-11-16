from math import factorial
n=int(input())
if n==0:
    print(1)
else:
    print(n*factorial(n-1))
    
