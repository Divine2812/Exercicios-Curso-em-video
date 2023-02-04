#Exercício 068 - Jogo par ou ímpar.
print('\033[33m-=' * 30 + '-\033[m')
print("\033[35mPar ou ímpar")
print('\033[33m-=' * 30 + '-\033[m')
import random
computador = random.randint(0, 10)
parouimpar = 0
while True:
    parouimpar = int(input("\033[34mDigite [1] para ÍMPAR;\nDigite [2] para PAR;\nDigite a sua escolha:\033[m "))   
    while parouimpar > 2 or parouimpar < 1:
        parouimpar = int(input("\033[31mNúmero inválido! Digite [1] para ÍMPAR ou [2] para PAR:\033[m "))
    jogador = int(input("\033[35mDigite um número:\033[m "))
    if parouimpar == 2:
        parouimparnome = "PAR"
    elif parouimpar == 1:
        parouimparnome = "ÍMPAR"
    print("-=-=-=-=-=-=-=-=-")
    soma = computador + jogador
    if soma % 2 == 0 and parouimpar == 2:
        print(f"\033[32mPAR!! Você ganhou. O computador jogou {computador} e a soma dos números deu {soma}.\033[m ")
    elif soma % 3 == 0 and parouimpar == 1:
         print(f"\033[32mÍMPAR!! Você ganhou. O computador jogou {computador} e a soma dos números deu {soma}.\033[m ")
    else:
        print(f"\033[31mVocê escolheu {parouimparnome}. O computador jogou {computador} e a soma dos números deu {soma}. Você perdeu :/\033[m")
        print('\033[33m-=' * 30 + '-\033[m')
        break
    print('\033[33m-=' * 30 + '-\033[m')
   