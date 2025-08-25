from random import randint

heads = 0
tails = 0

for i in range(1000):
    coin = randint(0, 1)
    if coin == 0:
        heads += 1
    else:
        tails += 1

print(f"heads: {heads}, el promedio de heads es {(heads / 1000)*100}%")
print(f"tails: {tails}, el promedio de tails es {(tails / 1000)*100}%")