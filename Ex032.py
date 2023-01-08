#Exercício 32 - Identificar se o ano inserido é um ano bissexto. 
import datetime
ano = int(input("Digite um ano qualquer: "))
if ano == 0:
    ano = datetime.date.today().year
#Se o ano inserido for 0, o programa irá usar o ano atual.
if ano % 4 == 0 and ano % 100!=0 or ano % 400 == 0:
    print("O ano inserido é um ano bissexto!")
else:
    print("O ano inserido nao é um ano bissexto.")
