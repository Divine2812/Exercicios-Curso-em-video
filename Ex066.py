#Exercício 066 - Ler vários números e usar break.
n1 = 0
n2 = 0
contador = 0
while n1 != 999:
    n1 = int(input("\033[34mDigite um número (\033[31m999 \033[34mpara parar o programa): \033[m"))
    if n1 == 999:
        break
    n2 += n1 
    contador += 1
if contador == 0:
    print("\033[31mNenhum número inserido para efetuar a soma. :/")
elif contador == 1:
    print("\033[31mApenas um número foi inserido...")
else:
    print(f"\033[35mA soma dos números inseridos é {n2}, já a quantidade de números é {contador}.")