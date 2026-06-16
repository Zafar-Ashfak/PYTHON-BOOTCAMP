
n = int(input("Enter a natural number here: "))

i = 1
sum1 = 0

# Prints first n natural number using while loop
while i <= n:
    sum1 += i
    i += 1

print(f"sum1 of first {n} natural number using while loop is: {sum1}")

# Prints first n natural number using for loop
sum1 = 0

for j in range(1, n + 1):
    sum1 += j

print(f"sum1 of first {n} natural number using for loop is: {sum1}")






