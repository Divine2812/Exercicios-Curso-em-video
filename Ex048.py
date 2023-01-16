#Exercício 048 - Criar um programa que some os multiplos de 3, ímpares entre 1 e 500.
s = 0
n = 0
for c in range (0,500):
    if c % 2 != 0 and c % 3 == 0:
        s += c
        n = n + 1
print(f"A soma de todos os {n} números ímpares multiplos de 3 é de {s}")
