#Exercício 082 - Ler vários números e informar se eles são pares ou ímpares.
numeros = []
par = []
impar = []
while True:
    numero = int(input("Digite um número: "))
    numeros.append(numero)
    if numero % 2 == 0:
        par.append(numero)
    else: 
        impar.append(numero)
    ask = input("Quer continuar? S/N ")
    if ask in "nN":
        break
print(f"""=-=-=-=-=-=-=-=-=-=-=
Os números inseridos foram: {numeros};
Números pares: {par}
Números ímpares: {impar}
=-=-=-=-=-=-=-=-=-=-=""")