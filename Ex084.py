#Exercício 084 - Cadastrar o nome e o peso de várias epssoas e mostrar no final a quantidade e uma lista com as pessoas mais leves e pesadas.
cadastro = []
total = []
totpessoas = 0
while True:
    cadastro.append(input("Nome: "))
    cadastro.append(input("Peso: "))
    total.append(cadastro[:])
    cadastro.clear()
    totpessoas += 1
    ask = input("Quer continuar? S/N ")
    if ask in "Nn":
        break
print(f"O total de pessoas é de {totpessoas}")
print(f"O maior peso foi de {max(total)[0].capitalize()} de {max(total)[1]} Kgs!")
print(f"O menor peso foi de {min(total)[0].capitalize()} de {min(total)[1]} Kgs!")
