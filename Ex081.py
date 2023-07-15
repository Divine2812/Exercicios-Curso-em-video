#Exercício 081 - Criar uma lista, informar se o valor 5 está nela ou não, mostrar quantos valores e a lista decrescente.
lista = []
while True:
    n = int(input("Digite um número: "))
    lista.append(n)
    print(lista)
    ask = input("Deseja continuar? S/N ")
    if ask in "nN":
        break

print(f"""=-=-=-=-=-=-=-=-=
Lista: {lista.sort(reverse = False)}
Foram digitados {len(lista)} números.
""")
if 5 in lista:
    print(f"Há o número 5 na posição {lista.index(5)}\n=-=-=-=-=-=-=-=-=")