#Exercício 052 - Ver se o número inserido é primo ou não.
from prime_test import prime
print('\033[33m-=' * 30 + '-\033[m')
print('\033[35mIdentificador de números primos.')
print('\033[33m-=' * 30 + '-\033[m')
n = int(input("Digite um número: "))
prime_result = prime.test(n)
if prime_result is True:
    print(f"O número {n} é um número primo.")
else:
   print(f"O número {n} não é um número primo.")
print('-=' * 30 + '-')



