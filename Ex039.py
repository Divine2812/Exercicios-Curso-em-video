#Exercício 039 - Alistamento militar
from datetime import date
print("\033[33m-=" * 30 + "-\033[m")
print("\033[36mAlistamento Militar - Ano de nascimento")
print("\033[33m-=" * 30 + "-\033[m")
ano = int(input("\033[36mDigite o ano de seu nascimento: "))
idd = date.today().year - ano

if idd < 18:
    falta = 18 - idd
    if falta == 1:
        print(f"\033[35mVocê ainda irá se alistar após {falta} ano") 
    else:
        print(f"\033[35mVocê ainda irá se alistar após {falta} anos")
elif idd == 18:
    print("\033[35mVocê já está com a idade mínima para servir.")
elif idd > 18:
    passou = idd - 18
    if passou == 1:
        print(f"\033[35mVocê passou do tempo de alistamento em {passou} ano.")
    else: 
        print(f"\033[35mVocê passou do tempo de alistamento em {passou} anos.\033[m")