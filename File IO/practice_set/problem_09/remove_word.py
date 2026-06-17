# Write a program that reads the content of a file and removes all occurrences of a given word with space.

def remove_word(filename, matching_word):
    with open(filename, "r") as file:
        data = file.read().lower()
        new_data = data.replace(matching_word, "")

    with open(filename, "a") as file:
        file.write(f"\n\nAfter Removing all occurrences of word '{matching_word}'\n\n")
        file.write(new_data)
        print("Removed all occurrences of a given word successfully")


def main():
    print("Program that removes all occurrences of a given word from a file")
    filename = "file.txt"
    word = "rabbit"
    remove_word(filename, word)

main()

