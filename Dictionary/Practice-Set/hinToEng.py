# Program to create a dictionary with hindi words with values as their english
# translation. Provide user with an option to look it up
words = {
    "जाना" : "Go",
    "आना": "Come",
    "खाना": "Eat",
    "पीना": "Drink",
    "देखना": "See",
    "सुनना": "Listen",
    "बोलना": "Speak",
    "पढ़ना": "Read",
    "लिखना": "Write",
    "सीखना": "Learn",
    "सिखाना": "Teach",
    "सोना": "Sleep",
    "उठना": "Wake/Get up",
    "चलना": "Walk",
    "दौड़ना": "Run",
    "बैठना": "Sit",
    "खड़ा होना": "Stand",
    "बनाना": "Make/Build",
    "देना": "Give",
    "लेना": "Take",
    "खोलना": "Open",
    "बंद करना": "Close",
    "पूछना": "Ask",
    "बताना": "Tell",
    "समझना": "Understand",
    "सोचना": "Think",
    "पसंद करना": "Like",
}

userInput = input("Enter a word in hindi: ")
print(f"{userInput} : {words.get(userInput)}")