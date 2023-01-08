#Exercício 18 - Mostrar o valor do seno, cosseno e tangente de um ângulo.
import math
ang = float(input("Digite um ângulo: "))
cos = math.cos(math.radians(ang))
sen = math.sin(math.radians(ang))
tang = math.tan(math.radians(ang))
print("=-=-=-=-=-=-=-=-=")
print(f"O cosseno, seno e a tangente de {ang} é, respectivamente: {cos}, {sen} e {tang}")
print("=-=-=-=-=-=-=-=-=")
