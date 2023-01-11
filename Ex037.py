#Exercício 037 - Conversos de número decimal para binário, octal e hexadecimal.
print("\033[33m-=" * 20 + "-\033[m")
print("Conversor de número decimal para binário, octal ou hexadecimal.")
print("-=" * 20 + "-")
num = int(input("Digite um número a ser convertido: "))
print("Digite 1 para converter o número inserido para binário;\nDigite 2 para converter o número inserido para octal;\nDigite 3 para converter o número inserido para hexadecimal.")
inf = int(input("Digite o número: "))
if inf == 1:
    b = bin(num)
    print(b.replace('0b', ""))
elif inf == 2:
    o = oct(num)
    print(o.replace('0o', ""))
elif inf == 3:
    h = hex(num)
    print(h.replace('0x', ""))