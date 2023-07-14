#Exercício 079 - Pedir números e adiciona-los em uma lista.
print("=-=-=-=-=-=-=-=")
lista = []
while True:
    numero = int(input("Digite um número: "))
    if numero in lista:
        print("Este número não foi adicionado.")
    elif numero not in lista:
        lista.append(numero)
        print("Número adicionado!")
    decisao = input("Quer continuar? S/N ")
    if decisao[0] in "Nn":
        break
print(f"Os números adicionados foram {sorted(lista)}.")
print("=-=-=-=-=-=-=-=")