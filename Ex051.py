#Exercício 051 - Ler o primeiro termo e a razão da P.A e informar os 10 primeiros termos.
print('\033[33m-=' * 30 + '-\033[m')
print("\033[35mMostrar os 10 primeiros termos de uma P.A.")
print('\033[33m-=' * 30 + '-\033[m')
a1 = int(input("Digite o primeiro termo da P.A: "))
r = int(input("Digite a razão da P.A: "))
pf = a1 + (10 - 1) * r + 1
lis = []
for c in range (a1, pf, r):
    lis.append(c)
sr = str(lis)
print(f"Os 10 primeiros números da P.A inserida são: {str(lis)[1:-1]}")
print('\033[33m-=' * 30 + '-\033[m')