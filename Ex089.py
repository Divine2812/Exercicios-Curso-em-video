#Exercício 089 - Média de alunos.
geral = []
temp = []
n = 0
while True:
    temp.append(str(input("Nome: ")))
    temp.append(float(input("Nota 1: ")))
    temp.append(float(input("Nota 2: ")))
    temp.append((temp[1]+temp[2])/2) 
    geral.append(temp[:])
    n +=1
    temp.clear()
    ask = input("Quer continuar? S/N ")
    if ask in "nN":
        break
print("-=" * 30 + "-")
print(f'{"Nº":<8}{"Nome":<10}{"Média":>8}')
for g, nome in enumerate(geral):
    print(f'{g+1:<8}{nome[0]:<10}{nome[3]:>8.1f}')
print("-=" * 30 + "-")
while True:
    ask2 = int(input("Mostrar as notas de qual aluno? (999 finaliza o programa) "))
    if ask2 == 999:
        print("Entendido! Programa finalizado.")
        break
    elif ask2 > n:
        print("Número inválido!")
    else:
        print(f"As notas do aluno {geral[ask2][0]} são: {geral[ask2][1]} e {geral[ask2][2]}")