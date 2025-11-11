import random

senha = []
cont = 0


while True:
    cont = cont + 1
    senha.append(random.randint(0,60))
    if cont == 6:
        break



print(senha)
