#Exercício 033 - Identificar os valores inseridos e informar o maior e o menor valor.
x = int(input("Digite o primeiro número: "))
y = int(input("Digite o segundo número: "))
z = int(input("Digite o terceiro número: "))
a = max(x, y, z)
print(f"O maior valor é: {a} e o menor valor é {min(x, y, z)}")
