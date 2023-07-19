#Exercício 080 - Inserir números em uma lista já em ordem.
lista = []
for num in range (0,5):
    numero = int(input("Digite um número: "))
    if num == 0 or numero > lista[-1]:
        lista.append(numero)
    else:
        pos = 0
        while pos < len(lista):
            if numero <= lista[pos]:
                lista.insert(pos, numero)
                break
            pos+=1
print(f"Os valores inseridos foram organizados em ordem: {lista}")