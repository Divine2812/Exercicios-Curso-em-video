#Exercício 046 - Contagem regressiva de fogos.
from time import sleep
import emoji
print('\033[33m-=' * 30 + '-\033[m')
print('\033[35mContagem regressiva dos fogos.')
print('\033[33m-=' * 30 + '-\033[m')
n = str(input("\033[35mDigite qualquer número para iniciar a contagem: "))
if n.isnumeric() == True:
    for c in range (10, 0, -1):
        print(c)
        sleep(1)
    print(emoji.emojize("\033[32mOs fogos começaram!!! :confetti_ball::confetti_ball::confetti_ball::dizzy::confetti_ball::confetti_ball::confetti_ball::confetti_ball::confetti_ball::confetti_ball::confetti_ball::confetti_ball::confetti_ball::confetti_ball::confetti_ball::confetti_ball::confetti_ball:\033[m"))
else: 
    print("\033[31mO caractere inserido não é um número.\033[m")

    