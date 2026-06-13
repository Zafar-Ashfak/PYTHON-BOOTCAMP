# Write a function that takes a filename and returns the number of vowels in that file.
def count_vowels(filename):
    with open(filename, "r") as file:
        data = file.read().lower()

        count = 0
        for ch in data:
            if ch in "aeiou":
                count += 1

        return count

res = count_vowels("python.txt")
print(f"Total number of vowels in the file 'python.txt' is: {res}")
