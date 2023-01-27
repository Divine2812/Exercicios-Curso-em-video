#Exercício 053 - Ver se a frase inserida é um políndromo.
f = str(input("Digite uma frase: "))
n = f.replace(' ', '')

if n.lower() == "".join(reversed(n.lower())):
    print("É um Políndromo.")
else: 
    print("Não é um polindromo.")

