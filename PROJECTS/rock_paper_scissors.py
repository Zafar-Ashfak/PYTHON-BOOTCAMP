import random

def main():
    print("🎮 ROCK PAPER SCISSORS GAME 🎮")
    print("📜Game Instruction: Enter r for Rock, p for Paper, tand s for Scissors📜\n")

    user_input = input("Enter your choice: ").lower()

    my_dict = {
        "r": -1,
        "p": 0,
        "s": 1
    }

    reverse_dict = {
        -1: "rock",
        0: "paper",
        1: "scissors"
    }

    if user_input not in my_dict:
        print("Invalid Input, please read the instruction")
        return

    computer = random.choice([-1, 0, 1])
    user = my_dict[user_input]

    print(f"You chose: {reverse_dict[user]}")
    print(f"Computer chose: {reverse_dict[computer]}\n\n")

    if computer == user:
        print("Game Draw")
    elif computer == -1 and user == 0:
        print("🏆 You Win 🏆")
    elif computer == -1 and user == 1:
        print("👎 You Lose 👎")
    elif computer == 0 and user == -1:
        print("👎 You Lose 👎")
    elif computer == 0 and user == 1:
        print("🏆 You Win 🏆")
    elif computer == 1 and user == -1:
        print("🏆 You Win 🏆")
    elif computer == 1 and user == 0:
        print("👎 You Lose 👎")

main()