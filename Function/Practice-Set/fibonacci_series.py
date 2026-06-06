# Write a function fibonacci(n) that returns the first n Fibonacci numbers.
print("Program to print first n fibonacci series")
def fibonacci_series(n):
    a = 0
    b = 1

    for i in range(n):
        print(a, end=" ")
        c = a + b
        a = b
        b = c

num = int(input("Enter a natural number: "))
fibonacci_series(num)