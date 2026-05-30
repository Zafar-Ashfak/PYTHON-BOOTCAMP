sentence = "Hello, I am  Md Ashfaq Alam."

print(sentence)
print(f"Double Space occurs at index: {sentence.find("  ")}")

removeSpace = sentence.replace("  ", " ")
print("\nString after replacing double space with single space")
print(removeSpace)