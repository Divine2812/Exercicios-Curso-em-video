#Exercício 053 - Ver se a frase inserida é um políndromo.
print('\033[33m-=' * 30 + '-\033[m')
f = str(input("Digite uma frase: "))
n = f.replace(' ', '')

if n.lower() == "".join(reversed(n.lower())):
    print("É um Políndromo.")
else: 
    print("Não é um polindromo.")
print('\033[33m-=' * 30 + '-\033[m')

