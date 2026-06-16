print("Program to print half pyramid by user's choice")
n = int(input("Enter a natural number: "))

for i in range(1, n + 1):
    for j in range(1, i + 1):
        print("*", end=" ")
    print()