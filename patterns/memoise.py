"""
memoization : with decorator

calculate the fibonacci number with and without fibbonacci without memoization
"""
def memoize(fn):
    memo={}
    def helper(x):
        """ cache"""
        if x not in memo:
            memo[x]=fn(x)
        return memo[x]
    return helper


@memoize
def fib(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fib(n-1)+fib(n-2)

print(fib(400))