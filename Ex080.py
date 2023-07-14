#Exercício 080 - Inserir números em uma lista já em ordem.
lista = []
for num in range (0,5):
    numero = int(input("Digite um número: "))
    if len(lista) == 0:
        lista.append(numero)
    elif len(lista) == 1:
        if numero > lista[0]:
            lista.append(numero)
        elif numero < lista[0]:
            lista.insert(0, numero)
    elif len(lista) == 2:
        if numero > lista[0] and numero < lista[1]:
            lista.insert(1, numero)
        elif numero < lista[0]:
            lista.insert(0, numero)
        elif numero > lista[1]:
            lista.append(numero)
    elif len(lista) == 3:
        if numero > lista[0] and numero < lista[1]:
            lista.insert(1, numero)
        elif numero > lista[1] and numero < lista[2]:
            lista.insert(2, numero)
        elif numero < lista[0]:
            lista.insert(0, numero)
        elif numero > lista[2]:
            lista.append(numero)
    elif len(lista) == 4:
        if numero > lista[0] and numero < lista[1]:
            lista.insert(1, numero)
        elif numero > lista[1] and numero < lista[2]:
            lista.insert(2, numero)
        elif numero > lista[2] and numero < lista[3]:
            lista.insert(3, numero)
        elif numero < lista[0]:
            lista.insert(0, numero)
        elif numero > lista[3]:
            lista.append(numero)
print(f"Os valores inseridos foram organizados em ordem: {lista}")