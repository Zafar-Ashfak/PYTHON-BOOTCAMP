p1 = "Make more money"
p2 = "buy now"
p3 = "subscribe my channel"
p4 = "click this"

comment = input("Enter your comment here: ")

if p1 in comment or p2 in comment or p3 in comment or p4 in comment:
    print("This is a spam comment")
else:
    print("This is not a spam comment")