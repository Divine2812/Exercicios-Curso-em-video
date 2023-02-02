#Exercício 058 - Versão 2.0 do exercício 028.
import random
numero_escolhido = random.randint(0,10)
contagem = 0
print(numero_escolhido)
print('\033[33m-=' * 30 + '-\033[m')
print(('\033[35mHummmm...\U0001f914\U0001f914 \nPensei em um número, tente adivinhar! hehe\033[m'))
print('\033[33m-=' * 30 + '-\033[m')
numero_inserido = int(input("\033[32mDigite um número entre 0 a 10: \033[m"))
while numero_inserido != numero_escolhido:
    numero_inserido = int((input("\033[31mNúmero incorreto! \U0001f614 Tente novamente:  \033[m")))
    contagem += 1
print((f"Acertou!! \U0001f389 \U0001f389 \U0001f389 \U0001f389 O número escolhido foi {numero_escolhido}.\033[m"))
print('\033[33m-=' * 30 + '-\033[m')