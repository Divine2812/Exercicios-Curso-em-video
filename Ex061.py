#Exercício 061 - Refazer o exercício 051 utilizando o while. 
print('\033[33m-=' * 30 + '-\033[m')
print("\033[35mMostrar os 10 primeiros termos de uma P.A. 2.0")
print('\033[33m-=' * 30 + '-\033[m')
primeiro_termo = int(input("Digite o primeiro termo da P.A: "))
razao = int(input("Digite a razão da P.A: "))
pf = primeiro_termo + (10 - 1) * razao + 1
lis = []
lis.append(primeiro_termo)
while len(lis) < 10:
    primeiro_termo += razao
    lis.append(primeiro_termo)
print(lis)
#for c in range (a1, pf, r):
#    lis.append(c)
print(f"Os 10 primeiros números da P.A inserida são: {str(lis)[1:-1]}")
print('\033[33m-=' * 30 + '-\033[m')