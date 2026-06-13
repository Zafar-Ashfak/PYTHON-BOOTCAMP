# Write a function that takes a filename and a word and returns how many times that word appears.
def count_specific_word(filename, specific_word):
    with open(filename, "r") as file:
        data = file.read().lower().split() # converts into list

        specific_word = specific_word.lower()

        count = 0
        for word in data:
            if word == specific_word or specific_word + "'s" == word:
                count += 1

        return count


def main():
    print("Program that takes a filename and a word and returns how many times that word appears")
    specific_word = "python"
    filename = "python.txt"
    res = count_specific_word(filename, specific_word)
    print(f"Word {specific_word} contains {res} times in the file {filename}")

main()