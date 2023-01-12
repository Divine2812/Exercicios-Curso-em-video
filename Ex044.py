#Exercício 044 - Calcular o valor a ser pago pelo produto.
print('\033[33m-=' * 30 + '-\033[m')
print("\033[35mCalcular o valor a ser pago pelo produto.")
print('\033[33m-=' * 30 + '-\033[m')
prec = float(input("\033[36mDigite o valor do produto: "))
print("\033[36mEscolha a opção de pagamento: ")
print("\033[36mDigite 1 para a opção de pagamento à vista/cheque; \nDigite 2 para a opção de pagamento à vista no cartão;\nDigite 3 para a opção de pagamento em até 2x no cartão;\nDigite 4 para a opção de pagamento em 3x ou mais no cartão.")
val = int(input("\033[36mDigite a opção de pagamento: "))
if val == 1:
    pag = (prec/100) * -10 + prec
    print(f"\033[35mA opção selecionada foi à vista/cheque com 10% de desc. O valor a ser pago pelo produto é de {pag}.\033[m")
elif val == 2:
    pag = (prec/100) * -5 + prec
    print(f"\033[35mA opção selecionada foi à vista no cartão com 5% de desc. O valor a ser pago pelo produto é de {pag}.\033[m")
elif val == 3:
    pag = val
    print(f"\033[35mA opção selecionada foi em até 2x no cartão. O valor a ser pago pelo produto é de {pag}.\033[m")
elif val == 4:
    pag = (prec/100) * 20 + prec 
    print (f"\033[35mA opção selecionada foi em 3x ou mais no cartão. O valor a ser pago pelo produto é de {pag}.\033[m") 
else: 
    print("\033[36mA opção inserida não existe.\033[m")
print('-=' * 30 + '-')

