#Exercício 047 - Mostrar todos os números pares de 1 a 50.
print('\033[33m-=' * 30 + '-\033[m')
print("Números pares entre 1 e 50.")
print('\033[33m-=' * 30 + '-\033[m')
l = []
for c in range (2 , 51, 2 ):
    l.append(c)
    #print(c, end=", ") -> Resolução feita pelo Gustavo Guanabara
print(str(l)[1:-1])
