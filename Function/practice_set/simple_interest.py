# Write a function simple_interest(p, r, t) that returns the simple interest.
print("Simple interest calculation program")
def simple_interest(p, r, t):
    return (p * r * t) / 100

principal = int(input("Enter the principal amount: "))
rate = int(input("Enter the rate of interest: "))
time = int(input("Enter the time period: "))
si = simple_interest(principal, rate, time)
print(f"SI = {si}")