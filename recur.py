def factorial(n):
    
    if n == 0:
        return 1
        
    return n * factorial(n - 1)   

def number_of_groups(n, k):

    return int(factorial(n) / (factorial(n-k) * factorial(k)))

def fibonacci(n):

    if n in (0, 1):
        return n

    return fibonacci(n-1) + fibonacci(n-2)



print(fibonacci(8))