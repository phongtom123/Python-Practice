import math

while True:
    print("==================")
    print("Area Calculator 📐")
    print("==================\n")

    print("1) Triangle")
    print("2) Rectangle")
    print("3) Square")
    print("4) Circle")
    print("5) Quit")

    shape = input("\nWhich shape: ")

    if shape == "1":
        base = float(input("Base: "))
        height = float(input("Height: "))
        area = (base * height) / 2
        print(f"\nThe area is {area}\n")

    elif shape == "2":
        length = float(input("Length: "))
        width = float(input("Width: "))
        area = length * width
        print(f"\nThe area is {area}\n")

    elif shape == "3":
        side = float(input("Side: "))
        area = side ** 2
        print(f"\nThe area is {area}\n")

    elif shape == "4":
        radius = float(input("Radius: "))
        area = math.pi * radius ** 2
        print(f"\nThe area is {area:.2f}\n")

    elif shape == "5":
        print("\nGoodbye!")
        break

    else:
        print("\nPlease choose a number from 1 to 5.\n")