 #Exercício 078 - Criar uma lista e informar o maior e o menor valor digitado.
lista = []
for c in range (1, 6):
    lista.append(int(input(f"Digite o número da posição {c}: ")))

print(f"Os valores inseridos na lista são: {lista}")
print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
print(f"- O maior valor é o número {max(lista)} na(as) posição(ões): ", end="") 
for i, v in enumerate(lista):
    if v == max(lista):
        print(f"{i}... ", end="")
print()
print(f"- O menor valor é o número {min(lista)} na(as) posição(ões): ", end='')
for i, v in enumerate(lista):
    if v == min(lista):
        print(f"{i}... ", end='')
print()
print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")




