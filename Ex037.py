#Exercício 037 - Conversos de número decimal para binário, octal e hexadecimal.
print("\033[33m-=" * 20 + "-\033[m")
print("\033[34mConversor de número decimal para binário, octal ou hexadecimal.")
print("\033[33m-=" * 20 + "-\033[m")
num = int(input("Digite um número a ser convertido: "))
print("\033[32mDigite 1 para converter o número inserido para binário;\nDigite 2 para converter o número inserido para octal;\nDigite 3 para converter o número inserido para hexadecimal.\033[m")
inf = int(input("Digite o número: "))
print("\033[33m-=" * 20 + "-\033[m")
if inf == 1:
    b = bin(num).replace('0b', "")
    print(f"Convertendo o número {num} em binário, temos: {b}")
elif inf == 2:
    o = oct(num).replace('0o', "")
    print(f"Convertendo o número {num} em octal, temos: {o}")
elif inf == 3:
    h = hex(num).replace('0x', "")
    print(f"Convertendo o número {num} em hexadecimal, temos: {h}")
elif inf > 3:
    print("O número inserido não corresponde a nenhuma opção acima. Reincie o programa.")
print("\033[33m-=" * 20 + "-\033[m")