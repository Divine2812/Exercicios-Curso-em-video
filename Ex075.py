#Exercício 075 - Ler 4 números do teclado e inserir em uma tupla.
print('\033[33m-=' * 30 + '-\033[m')
print("\033[35mNão sei o que botr aqui kkkk.")
print('\033[33m-=' * 30 + '-\033[m')
n1 = int(input("Digite um número: "))
n2 = int(input("Digite um número: "))
n3 = int(input("Digite um número: "))
n4 = int(input("Digite um número: "))
tuprarsrs = n1, n2, n3, n4
rs = numeronove = 0
listanumerospar = []
for c in range (0, 4):
    if tuprarsrs[rs] == 9:
        numeronove += 1
    if tuprarsrs[rs] % 2 == 0:
        listanumerospar.append(tuprarsrs[rs])
    rs += 1
if numeronove > 0:
    print(f"A quantidade de vezes que aparece o número nove é de: {numeronove}")
else:
    print("O número 9 não aparece nenhuma vez.")
if 3 in tuprarsrs:
    posicao = tuprarsrs.index(3)
    if posicao >= 0:
        print(f"A primeira vez que o número 3 aparece é na posição: {posicao}")
else: 
    print("O número 3 não aparece em nenhuma posição.")

if len(listanumerospar) == 1:
    print(f"O número pare inserido é: {str(listanumerospar)[1:-1]}")
elif len(listanumerospar) > 1:
    print(f"Os números pares inseridos são: {str(listanumerospar)[1:-1]}")
elif len(listanumerospar) == 0:
    print("Não há nenhum número par.")
print('\033[33m-=' * 30 + '-\033[m')