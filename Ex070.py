#Exercício 070 - Programa que peã o nome e o preço dos produtos.
print('\033[33m-=' * 12 + '-\033[m')
print("\033[35m      Lojas Divinas")
print('\033[33m-=' * 12 + '-\033[m')
nomesprodutos = []
precos = []
total = 0
c = 0
while True:
    nome = input("\033[34mDigite o nome do produto:\033[m ")
    nomesprodutos.append(nome)
    preco = float(input("\033[34mDigite o preço do produto:\033[m "))
    precos.append(preco)
    if preco >= 1000:
        c += 1
    total += preco
    resposta = input("\033[34mQuer continuar? S/N \033[m").upper().strip()[0]
    while resposta not in "SN":
        resposta = input("\033[31mOpção inválida! Digite S ou N:\033[m ")
    print("-=-=-=-=-=-=-=-=-=-")
    if resposta == 'N':
        break
f = precos.index(min(precos))

print(f"""\033[35mO total gasto na compra foi:\033[m R${total:.2f};
\033[35mHá {c} produtos custando mais que \033[mR$1000,00;
\033[35mO produto mais barato é \033[m{nomesprodutos[f]}\033[35m custando \033[mR${min(precos):.2f}\033[35m.\033[m""")
print('\033[33m-=' * 12 + '-\033[m')