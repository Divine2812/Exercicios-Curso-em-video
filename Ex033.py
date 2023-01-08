#Exercício 033 - Identificar os valores inseridos e informar o maior e o menor valor.
x = int(input("\033[33mDigite o primeiro número: "))
y = int(input("\033[33mDigite o segundo número: "))
z = int(input("\033[33mDigite o terceiro número: "))
a = max(x, y, z)
print("\033[36m-=" * 20 + "\033[36m-\033[m")
print(f"O maior valor é: \033[31m{a}\033[m e o menor valor é \033[31m{min(x, y, z)}\033[m.")
print("\033[36m-=" * 20 + "\033[36m-\033[m")

