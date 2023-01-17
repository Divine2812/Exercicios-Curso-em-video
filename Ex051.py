#Exercício 051 - Ler o primeiro termo e a razão da P.A e informar os 10 primeiros termos.
print('\033[33m-=' * 30 + '-\033[m')
print("\033[35mMostrar os 10 primeiros termos de uma P.A.")
print('\033[33m-=' * 30 + '-\033[m')
a1 = int(input("Digite o primeiro termo da P.A: "))
r = int(input("Digite a razão da P.A: "))
for c in range (0, 10, r):
    print(c)