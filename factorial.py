#python program to calculate factorial of a number using recursion
def factorial(n):
    if n < 2:

        return n
    return n * factorial(n-1)
print(factorial(6))
