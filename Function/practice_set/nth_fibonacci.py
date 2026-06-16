# Write a function fibonacci(n) that returns the nth Fibonacci number given by user.

def nth_fibonacci(n):
    a = 0
    b = 1

    if n == 0:
        return a
    elif n == 1:
        return b

    for i in range(2, n + 1):
        c = a + b
        a = b
        b = c

    return b

print("Program to calculate nth fibonacci")
num = int(input("Enter a number: "))
print(nth_fibonacci(num))

# 0 1 1 2 3 5 8 13 21