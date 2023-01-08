#Exercício 028 - Criar um programa que escolha um número de 0 a 5 e diga se o número que o usuário inseriu é o mesmo.
import random
n = random.randint(0,5)
print("Adivinhe o número de 0 a 5 que eu pensei. ")
s = int(input("Digite um número entre 0 a 5: "))
if s == n:
    print(f"Parabéns, você acertou! O número correto era {n},")
else:
    print(f"Número errado. O número correto foi {n}. =(")
