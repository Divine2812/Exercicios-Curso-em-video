#Exercício 050 - Ler 6 números inteiros e somar apenas os números pares. 
s = 0
for c in range (0, 6):
    n = int(input("Digite um número inteiro: "))
    if n % 2 == 0:
        s += n
print(f"Somando apenas os números pares inseridos, a soma vai dar: {s}")
