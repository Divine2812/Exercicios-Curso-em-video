#Exercício 053 - Ver se a frase inserida é um políndromo.
print('\033[33m-=' * 30 + '-\033[m')
f = str(input("Digite uma frase: ")).strip().upper()
n = f.replace(' ', '')
a = ""

if n.lower() == "".join(reversed(n.lower())):
    print("É um Políndromo.")
else: 
    print("Não é um polindromo.")
print('\033[33m-=' * 30 + '-\033[m')

#Outra forma: 
for c in range(len(n)-1, -1, -1):
    a += n[c]
if a == n:
    print(f"A frase {a} é um políndromo.")
else:
    print(f"A frase {f} fica {a}, não sendo um políndromo.")
