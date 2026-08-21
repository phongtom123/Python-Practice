import random

print("==========================")
print("🌌 Escape from Planet Zora")
print("==========================\n")

print("Your spaceship crashed on Planet Zora!")
print("You must find a way to escape.\n")

health = 100

while health > 0:
    print("Where do you want to go?")
    print("1) Explore the dark forest")
    print("2) Search the abandoned spaceship")
    print("3) Try to send a rescue signal")
    print("4) Give up")

    choice = input("\nChoose 1-4: ")

    if choice == "1":
        print("\nYou enter the dark forest...")

        monster = random.randint(1, 2)

        if monster == 1:
            health -= 30
            print("A space monster attacks you! You lose 30 HP.")
            print(f"Health: {health}\n")
        else:
            print("You find a magic crystal. It shows you the way home!")
            print("🎉 You won the game!")
            break

    elif choice == "2":
        print("\nYou search the abandoned spaceship.")
        print("You find fuel for your ship!")
        print("🚀 You escape Planet Zora. You won!")
        break

    elif choice == "3":
        print("\nYou send a rescue signal...")

        rescue = random.randint(1, 2)

        if rescue == 1:
            print("A rescue ship receives your signal!")
            print("🎉 You are saved. You won!")
            break
        else:
            health -= 20
            print("No one receives the signal. You lose 20 HP.")
            print(f"Health: {health}\n")

    elif choice == "4":
        print("\nYou gave up. Game over!")
        break

    else:
        print("\nInvalid choice. Please enter a number from 1 to 4.\n")

if health <= 0:
    print("\nYour health reached 0. Game over!")