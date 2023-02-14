#Exercício 071 - Simular um caixa eletrônico.
from time import sleep
print('\033[33m-=' * 12 + '-\033[m')
print("\033[35m      Banco Divino")
print('\033[33m-=' * 12 + '-\033[m')
total = int(input("\033[34mDigite o valor a ser sacado: \033[m"))
céd = 50
qnt = 0
sleep(1)
print("Analizando dados...")
sleep(1)
while True:
    if total >= céd:
        total -= céd
        qnt += 1
    else:
        if qnt > 0:
            print(f"\033[35mO total de notas de {céd} é de {qnt}.\033[m")
            qnt = 0
        if céd == 50:
            céd = 20
        elif céd == 20:
            céd = 10
        elif céd == 10:
            céd = 1
        if total == 0:
            break
print("\033[31mPrograma finalizado!")
print('\033[33m-=' * 12 + '-\033[m')