#Exercício 077 - Criar uma tupla com várias palavras e informar as vogais.
palavras = ("oi", "cavalo", "abecedario", "pedra", "tesoura", "fogos", "contabilidade", "atratividade", "taxa", "imposto", "governo", "salário")
f = 0
print("\033[33m -=-=-=-=-=-=-=-=-\033[m")
print("\033[35mVogais em palavras.")
print("\033[33m -=-=-=-=-=-=-=-=-\033[m")
print("-"*20)
for c in palavras:
    print(f"Na palavra '{c}', temos:", end= '')
    for letra in c:
        if letra in "aeiou":
            print('\033[31m ', end= letra + '\033[m')

    print("\n--------------------")