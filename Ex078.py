 #Exercício 078 - Criar uma lista e informar o maior e o menor valor digitado.
lista = []
for c in range (1, 6):
    lista.append(int(input(f"Digite o número da posição {c}: ")))

print(f"""Os valores inseridos na lista são: {lista}
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
- O maior valor é o número {max(lista)} na posição {lista.index(max(lista))} 
- O menor valor é o número {min(lista)} na posição {lista.index(min(lista))}
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=""")




