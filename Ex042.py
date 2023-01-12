#Exercício 042 - Refazer o desafio 35 e dizer se formam um triângulo isósceles, equilátero
l1 = float(input("Primeiro Segmento: "))
l2 = float(input("Segundo Segmento: "))
l3 = float(input("Terceiro Segmento: "))
print("\033[33m=\033[m" * 40)
if l1 + l2 <= l3 or l1 + l3 <= l2 or l2 + l3 <= l1:
    print("As medidas inseridas não formam um triângulo!")
else:
    if l1 == l2 and l2 == l3:
        eq = 'equilátero'
    elif l1 == l2 or l1 == l2 or l3 == l2 or l3 == l1:
        eq = "isósceles"
    elif l1 != l2 and l2 != l3:
        eq = "escaleno"
    print(f"As medidas inseridas \033[4;32mformam\033[m um triângulo {eq}. =D")
print("\033[33m=\033[m" * 40)
