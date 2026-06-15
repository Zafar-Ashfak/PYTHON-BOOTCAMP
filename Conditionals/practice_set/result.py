marks = int(input("Enter the marks of your subject: "))

if marks > 100:
    print("Invalid marks")
elif marks >= 33:
    print("PASS")
else:
    print("FAIL")