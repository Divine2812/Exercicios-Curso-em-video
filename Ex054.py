#Exercício 054 - Ler o ano de nascimento de 7 pessoas e dizer quais são maiores de idade. 
from datetime import date #datetime é usado para ver o ano atual
from more_itertools.recipes import unique_everseen #unique_everseen é usado para não ter anos repetidos nas listas.
print('\033[33m-=' * 30 + '-\033[m')
age_list18 = []
age_list0 = []
for c in range (1, 8):
    age = int(input("Digite o ano de nascimento: "))
    if date.today().year - age >= 18 :
        age_list18.append(age)
    else: 
        age_list0.append(age)
plus18 = list(unique_everseen(sorted(age_list18)))
ls18 = list(unique_everseen(sorted(age_list0))) #O sort coloca os anos em ordem crescente, fica mais bonitinho rs.
if len(age_list0) == 0:
    print(f"Os anos de nascimento das pessoas que são maiores de idade são: {str(plus18)[1:-1]}!")
    print(f"Nenhum ano inserido é menor de idade")
elif len(age_list18) == 0:
    print("Nenhum ano inserido é maior de idade")
    print(f"Os anos de nascimento das pessoas que são menores de idade são: {str(ls18)[1:-1]}!")
else: 
    print(f"Os anos de nascimento das pessoas que são maiores de idade são: {str(plus18)[1:-1]}!")
    print(f"Os anos de nascimento das pessoas que são menores de idade são: {str(ls18)[1:-1]}!")
print('\033[33m-=' * 30 + '-\033[m')
