sentence = "Hello, I am          Md Ashfaq Alam. And I am a senior software engineer."

print(sentence)
print(f"White Space occurs at index: {sentence.find("  ")}")

removeSpace = sentence.replace("          ", " ")
print("\nString after replacing white space with single space")
print(removeSpace)