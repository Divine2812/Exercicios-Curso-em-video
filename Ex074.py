#Exercício 074 - Sortear números
print('\033[33m-=' * 30 + '-\033[m')
print("\033[35mNúmeros aleatórios em tupla.")
print('\033[33m-=' * 30 + '-\033[m')
from random import randint
a = int(randint(0, 10000)), int(randint(0, 10000)), int(randint(0, 10000)), int(randint(0, 10000)), int(randint(0, 10000))
print(f"O maior número gerado é: {max(a)}")
print(f"O menor número gerado é: {min(a)}")
print(f"A lista de números gerados foi: {a[0]}, {a[1]}, {a[2]}, {a[3]} e {a[4]}")