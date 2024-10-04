def fib(n):
    if n == 0 or n == 1:
        return 1
    else:
        sum = fib(n - 1) + fib(n - 2)  
        return sum
print(fib(5))