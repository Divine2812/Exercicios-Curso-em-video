#Exercício 076 - Colocar dados em uma única tupla e informar os valores em forma de tabela.
nomes = ("Lápis", 1.75, 
         "Borracha", 2.00,
         "Caderno", 15.90,
         "Estojo", 25.00,
         "Transferidor", 4.20,
         "Compasso", 9.99,
         "Mochila", 120.32,
         "Caneta", 22.30, 
         "Livro", 34.90)
print("-"*20)
print("Lista de preços!")
print("-"*20)
for c in range(len(nomes)):
    if type(nomes[c]) == str:
        print(f"{nomes[c]}.{'.' * (15 - len(nomes[c]))} R$ {nomes[c+1]:.2f}")
print("-"*20)