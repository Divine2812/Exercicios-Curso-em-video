#Exercício 062 - P.A 3.0
print('\033[33m-=' * 30 + '-\033[m')
print("\033[35mTermos de uma P.A. 3.0")
print('\033[33m-=' * 30 + '-\033[m')
primeiro_termo = int(input("\033[34mDigite o primeiro termo da P.A:\033[m "))
razao = int(input("\033[34mDigite a razão da P.A:\033[m "))
quantidade_termos = int(input("\033[34mDigite a quantidade de termos que deseja mostrar:\033[m "))
lis = []
lis.append(primeiro_termo)
contador = 0
while len(lis) < quantidade_termos:
    primeiro_termo += razao
    contador += 1
    lis.append(primeiro_termo)
    if len(lis) == quantidade_termos:
        print(f"\033[34mOs {quantidade_termos} termos da P.A inserida são: {str(lis)[1:-1]}")
        quantidade_termos = int(input("\033[34mDeseja mostrar mais quantos termos?\033[m "))
        list.clear(lis)
if quantidade_termos == 0:
    print(f"\033[31mPrograma finalizado! {contador + 1} termos informados.\033[m")
print('\033[33m-=' * 30 + '-\033[m')