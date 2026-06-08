 # Write a program to calculate the power of a number
def power(b, e):
     #ase Case
     if e == 0:
         return 1

     # Work
     return b * power(b, e - 1)

def main():
    print("Program to calculate the power of a number")
    b = int(input("Enter base: "))
    e = int(input("Enter exponent: "))
    res = power(b, e)
    print(f"{b} ^ {e} = {res}")

main()