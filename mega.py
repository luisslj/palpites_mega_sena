import random

mega = []
cont = 0
palpite = []


while True:
    cont = cont + 1
    mega.append(random.randint(0,60))
    palpite.append(random.randint(0,60))
    if cont == 6:
        break

while True:
    if mega == palpite:
        break
    print(mega)

print(mega)
print(palpite)
