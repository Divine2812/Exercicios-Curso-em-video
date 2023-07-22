#Exercício 084 - Cadastrar o nome e o peso de várias epssoas e mostrar no final a quantidade e uma lista com as pessoas mais leves e pesadas.
cadastro = []
total = []
mai = men = 0
while True:
    cadastro.append(str(input("Nome: ")))
    cadastro.append(float(input("Peso: ")))
    total.append(cadastro[:])
    if len(total) == 1:
        mai = men = cadastro[1]
    else: 
        if cadastro[1] > mai:
            mai = cadastro[1]
        if cadastro[1] < men:
            men = cadastro[1]
    cadastro.clear()
    ask = input("Quer continuar? S/N ")
    if ask in "Nn":
        break
mais = []
menos = []
for p in total:
    if p[1] == mai:
        mais.append(p[0])
    if p[1] == men:
        menos.append(p[0])
print("-="*30+"-=")
if len(mais) > 1:
    estilo = ("das", "pessoas")
else:
    estilo = ("da", "pessoa")
if len(menos) > 1:
    estilomenos = ("das", "pessoas")
else:
    estilomenos = ("da", "pessoa")
print(f"O total de pessoas é de {len(total)}.")
print(f"O maior peso foi de {mai} Kgs {estilo[0]} {estilo[1]}: {mais} ")
print(f"O menor peso foi de {men} Kgs {estilomenos[0]} {estilomenos[1]}: {menos}")
print("-="*30+"-=")
