#Exercício 045 - Pedra, papel e tesoura.
import random
from time import sleep
print('\033[33m-=' * 30 + '-\033[m')
print('\033[35mPedra, papel e tesoura começando...')
pedra = 'pedra'
tesoura = 'tesoura'
papel = 'papel'
print('\033[33m-=' * 30 + '-\033[m')
print("Escolha entre as opções abaixo: \nDigite 1 para escolher PEDRA;\nDigite 2 para escolher TESOURA;\nDigite 3 para escolher PAPEL.")
esc = int(input("Digite uma opção acima: ")) 
sleep(1)
print("PEDRA...")
sleep(1)
print("PAPEL...")
sleep(1)
print("TESOURA!")
sleep(1)
if esc == 1:
    esc = pedra
elif esc == 2:
    esc = tesoura
elif esc == 3:
    esc = papel
list = (pedra, tesoura, papel)
ran = random.choice(list)
if esc == ran or ran == esc:
    print(f"\033[35mO computador jogou {ran} e você jogou {esc}. Deu empate!")
elif esc == pedra and ran == tesoura:
    print(f"\033[35mO computador jogou {ran} e você jogou {esc}. Você ganhou! =D")
elif esc == tesoura and ran == pedra:
    print(f"\033[31mO computador jogou {ran} e você jogou {esc}. Você perdeu! =(")
elif esc == papel and ran == tesoura:
     print(f"\033[31mO computador jogou {ran} e você jogou {esc}. Você perdeu! =(")
elif esc == pedra and ran == papel:
     print(f"\033[31mO computador jogou {ran} e você jogou {esc}. Você perdeu! =(")
elif esc == papel and ran == pedra:
    print(f"\033[35mO computador jogou {ran} e você jogou {esc}. Você ganhou! =D")
elif esc == tesoura and ran == pedra:
    print(f"\033[35mO computador jogou {ran} e você jogou {esc}. Você ganhou! =D")
elif esc == tesoura and ran == papel:
     print(f"\033[35mO computador jogou {ran} e você jogou {esc}. Você ganhou! =D =(")
print('\033[m-=' * 30 + '-')
