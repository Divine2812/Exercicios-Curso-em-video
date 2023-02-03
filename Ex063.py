#Exercício 063 - Sequência Fibonacci.
print('\033[33m-=' * 30 + '-\033[m')
print("\033[35mSequência Fibonacci")
print('\033[33m-=' * 30 + '-\033[m')
quantidade_termos = int(input("\033[34mDigite a quantidade de termos:\033[m "))
sequencia = [0, 1]
while quantidade_termos >= (len(sequencia)-1):
    n1 = sequencia[-1]
    n2 = sequencia[-2]
    continuacao = n1 + n2
    sequencia.append(continuacao)
if quantidade_termos == 1:
    print(f"\033[31mO {quantidade_termos}º termo solicitado é:\033[m {sequencia[0]}")
elif quantidade_termos == 2:
     print(f"\033[31mOs {quantidade_termos} termos solicitados são:\033[m 0, 1")
else:
    print(f"\033[31mOs {quantidade_termos} termos solicitados são:\033[m {str(sequencia)[1:-1]}")
print('\033[33m-=' * 30 + '-\033[m')


    