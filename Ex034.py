#Exercício 034 - Calcular o aumento de salário com as diferentes porcentagens
n = float(input("Digite o número do salário a ser acrescido: "))
print("\033[31m=\033[m" * 50)
if n<=1250:
    au = (n/100)*15
    print(f"O aumento salarial foi de \033[1;33m{au:.2f}\033[mR$, totalizando \033[1;33m{au+n:.2f}\033[mR$!")
else:
    au2 = (n/100)*10
    print(f"O aumento salarial foi de \033[1;33m{au2:.2f}\033[mR$, totalizando \033[1;33m{au2+n:.2f}\033[mR$!")
print("\033[31m=\033[m" * 50)
