#Exercício 052 - Ver se o número inserido é primo ou não.
print('\033[33m-=' * 30 + '-\033[m')
print('\033[35mIdentificador de números primos.')
print('\033[33m-=' * 30 + '-\033[m')
n = int(input("Digite um número: "))
if n < 2 or n > 2 and n % 2 == 0:
    print(f"O número {n} não é um número primo.")
elif n == 2:
    print(f"O número {n} é um número primo.")
else:
    for c in range (3, n):
        if n % c == 0:
            print(f"O número {n} não é um número primo.")
    print(f"O número {n} é um número primo")
print('-=' * 30 + '-')

