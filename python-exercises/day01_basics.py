# Write code below 💖
pesos = int(input("What do you have left in pesos?"))
soles = int(input("What do you have left in lesos?"))
reais = int(input("What do you have left in reais?"))

usd = (pesos * 0.00032) + (soles * 0.30) + (reais * 0.20)
print(f"{usd:.2f}")