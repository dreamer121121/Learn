def Fibonacci(self, n):
    # write code here
    result = [0, 1]
    if n < 2:
        return result[n]
    else:
        fib1 = 0
        fib2 = 1
        fibn = 0
        i = 2
        while i <= n:
            fibn = fib1 + fib2
            fib1 = fib2
            fib2 = fibn
        return fibn
