year = int(input("Enter a year here: "))

a = year % 4 == 0
b = year % 100 != 0
c = year % 400 == 0

if a and b or c:
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")