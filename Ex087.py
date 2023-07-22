#Exercício 087 - Aprimorar o Exercício anterior.
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
s = n = 0
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f"Digite um valor para a posição [{l}, {c}]: "))
        if matriz[l][c] % 2 == 0:
            n += matriz[l][c]
        if c == 2:
            s += matriz[l][c]
print("=-=-=-=-=-=-=-=-=-=-=-=")
for l in range(0,3):
    for c in range(0,3):
        print(f"[ {matriz[l][c]:^5} ]", end="")
    print()
print("=-=-=-=-=-=-=-=-=-=-=-=")
print(f"A soma dos números pares é {n}.")
print(f'A soma dos números da terceira coluna é {s}.')
print(f'O maior valor da segunda linha é {max(matriz[1])}.')
print("=-=-=-=-=-=-=-=-=-=-=-=")