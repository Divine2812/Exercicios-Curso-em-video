#Exercício 085 - Organizar os números inseridos em pares e ímpares em ordem crescente.
temp = [[], [], []]
for c in range(1, 8):
    valor = int(input(f"Digite o {c}º número: "))
    temp[0].append(valor)
    if valor % 2 == 0:
        temp[1].append(valor)
    elif valor % 2 > 0:
        temp[2].append(valor)
print(f"Os números inseridos foram: {temp[0]}")
temp[1].sort()
print(f'Os números par são: {temp[1]}')
temp[2].sort()
print(f'Os números ímpares são: {temp[2]}')