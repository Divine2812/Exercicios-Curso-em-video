#Exercício 036 - Aprovando ou negando um empréstimo
print("\033[1;33m-=" * 20 + "\033[1;33m-\033[m")
print("\033[1;32mAvaliador de empréstimos.")
print("\033[1;33m-=" * 20 + "\033[1;33m-\033[m")
val = float(input("\033[32mPara começarmos a avaliar a possibilidade de um empréstimo, digite o valor da casa: \033[m"))
sal = float(input("\033[32mAgora, digite o seu salário: \033[m"))
ano = int(input("\033[32mDigite o tempo, em anos, em que o empréstimo será pago: \033[m"))
print("\033[31mAvaliando a possibilidade de empréstimo...\033[m")
parc = val/(ano * 12) 
porc = (sal/100) * 30
print("\033[1;33m-=" * 20 + "\033[1;33m-\033[m")
if parc > porc:
    print("\033[31mInfelizmente seu empréstimo foi \033[4;33mnegado\033[0;31m. \nA parcela de seu empréstimo é maior que 30% de seu salário. ")
else: 
    print(f"\033[32mSeu empréstimo foi \033[4;32aprovado\033[32m! O total da parcela mensal foi definida em \033[4;33m{parc:.2f}\033[0;32mR$!")
print("\033[1;33m-=\033[m" * 20 + "\033[1;33m-\033[m")
