#Exercício 022 - Analisar o nome digitado e mostrar ele em letras maiúsculas, minúsculas, a quantidade de letras do primeiro e de todo o nome e o primeiro nome.
n = str(input("Digite seu nome: ")).strip()
n1 = (n.replace(" ", ""))
n2 = len(n1)
spl = str.split(n)
print(f"Nome em letras maiúsculas: {n.upper()}")
print(f"Nome em letras minúsculas: {n.lower()}")
print(f"A quantidade total de letras é de {n2} letras!")
print(f"O primeiro nome é {spl[0]}.")
print(f"A quantidade de letras do primeiro nome é de {len(spl[0])} letras!")