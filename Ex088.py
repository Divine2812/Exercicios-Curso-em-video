#Exercício 088 - Criar palpites da Mega Sena.
from random import randint
from time import sleep
print("""=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
PALPITES MEGA SENA
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=""")
palpites = []
temp = []
ask = int(input("Digite quantos palpites o programa irá criar: "))
for c in range(0,ask):
    for p in range(0,6):
        num = randint(1,60)
        if num not in temp:
            temp.append(num)
        else:
            while num in temp:
                num = randint(1,60)
                if num not in temp:
                    temp.append(num)
                    break
    palpites.append(temp[:])
    temp.clear()
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
for num, pal in enumerate(palpites):
    pal.sort()
    print(f"Jogo {num+1} -> {pal}")
    sleep(1)
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')