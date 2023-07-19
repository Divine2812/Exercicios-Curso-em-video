#Exercício 081 - Criar uma lista, informar se o valor 5 está nela ou não, mostrar quantos valores e a lista decrescente.
lista = []
while True:
    lista.append(int(input("Digite um número: ")))
    ask = input("Deseja continuar? S/N ")
    if ask in "nN":
        break
lista.sort(reverse=True)
print(f"""=-=-=-=-=-=-=-=-=
Lista: {lista}
Foram digitados {len(lista)} números.""")
if 5 in lista:
    print(f"Há o número 5 na posição {lista.index(5)}\n=-=-=-=-=-=-=-=-=")
else:
    print("O número 5 não aparece na lista.")