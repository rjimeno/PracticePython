#!/usr/bin/env python3

n = int(input("How many Fibonacci numbers?: "))

def f(n):
    if n < 1:
        exit(1)
    elif n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return f(n-2)+f(n-1)

result=[]
for i in range(1, n+1):
    result.append(f(i))

print(result)
