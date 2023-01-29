#Exercício 055 - Ler o peso de 5 pessoas e dizer o maior e o menor peso. 
print('\033[33m-=' * 30 + '-\033[m')
pes = []
for peso in range (0, 5):
    m = float(input("Digite o peso a ser analisado: "))
    pes.append(m)
print(f"O maior peso inserido foi {max(pes):.2f} e o menor peso foi {min(pes):.2f}.")
print('\033[33m-=' * 30 + '-\033[m')
