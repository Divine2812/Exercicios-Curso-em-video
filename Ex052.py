#Exercício 052 - Ver se o número inserido é primo ou não.
print('\033[33m-=' * 30 + '-\033[m')
print('\033[35mIdentificador de números primos.')
print('\033[33m-=' * 30 + '-\033[m')
n = int(input("Digite um número: "))
for c in range (2, 100):
    k = n % c
if k > 0 and n / n == 1 and n / 1 == n or n == 2 or n == 3:
    print(f"O número {n} é um número primo.")
else:
   print(f"O número {n} não é um número primo.")
print('-=' * 30 + '-')


