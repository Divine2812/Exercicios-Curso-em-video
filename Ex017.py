#Exercício 17 - Calcular  hipotenusa de um triângulo retângulo.
import math
cat1 = float(input("Digite o comprimento de um dos catetos: "))
cat2 = float(input("Digite o comprimento de outro cateto: "))
hip = math.sqrt(math.pow(cat1,2)+math.pow(cat2,2))
print("=-=-=-=-=-=-=-=-=-=")
print(f"A hipotenusa é {hip}")
print("=-=-=-=-=-=-=-=-=-=")