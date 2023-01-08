#Exercício 035 - Ver o tamanho dos traços inseridos e informar se é possível fazer um triângulo.
l1 = float(input("Primeiro Segmento: "))
l2 = float(input("Segundo Segmento: "))
l3 = float(input("Terceiro Segmento: "))
print("\033[33m=\033[m" * 40)
if l1 + l2 <= l3 or l1 + l3 <= l2 or l2 + l3 <= l1:

    print("As medidas inseridas \033[4;31mnão formam\033[m um triângulo! =(")
else:
    print("As medidas inseridas \033[4;32mformam\033[m um triângulo. =D")

print("\033[33m=\033[m" * 40)
#Exercício com cores
