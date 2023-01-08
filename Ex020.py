#exercício 20 - organizar uma lista com os nomes inseridos e sortea-los.
import random
n1 = input("Digite o nome do primeiro aluno: ")
n2 = input("Digite o nome do segundo aluno: ") 
n3 = input("Digite o nome do terceiro aluno: ")
n4 = input("Digite o nome do quarto aluno: ") 
list = random.sample([n1, n2, n3, n4], k=4)

print(f"A ordem da apresentação foi definida em: {list[0]}, {list[1]}, {list[2]} e {list[3]}!")
