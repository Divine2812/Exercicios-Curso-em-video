#Exercício 060 - Calcular o fatorial do número inserido.
from time import sleep
print('\033[33m-=' * 20 + '-\033[m')
print("\033[35m       Calculadora de fatorial")
print('\033[33m-=' * 20 + '-\033[m')
n = int(input("Digite um número a ser calculado: "))
fatorial = n
f = n
sleep(1)
print(f"Calculando o fatorial do número {n}...")
sleep(1)
while fatorial > 0:
    print(fatorial, end="")
    print(' x ' if fatorial > 1 else ' = ', end='')
    fatorial -= 1
    if fatorial > 0:
        f *= fatorial    
print(f)
print('\033[33m-=' * 20 + '-\033[m')
    
