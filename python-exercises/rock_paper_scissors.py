import random

print("===================")
print("Rock Paper Scissors")
print("===================\n")

print("1) ✊")
print("2) ✋")
print("3) ✌️")

player = int(input("Pick a number: "))

if player < 1 or player > 3:
    print("Wrong input")
else:
    computer = random.randint(1, 3)

    choices = {
        1: "✊",
        2: "✋",
        3: "✌️"
    }

    print(f"\nYou chose: {choices[player]}")
    print(f"CPU chose: {choices[computer]}")

    if player == computer:
        print("It's a tie!")
    elif (
        (player == 1 and computer == 3) or
        (player == 2 and computer == 1) or
        (player == 3 and computer == 2)
    ):
        print("The player won!")
    else:
        print("The CPU won!")