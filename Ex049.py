#Exercício 049 - Fazer a tabuada de qualquer número usando laço.
print('\033[33m-=' * 30 + '-\033[m')
print('\033[35mTabuada.')
print('\033[33m-=' * 30 + '-\033[m')
c1 = int(input("Digite um número: "))
print(f"Tabuada do número {c1}...")
for c in range (0, 9):
    q = c + 1
    n = c1 * q
    print(f"{c1} x {q}  = {n}")
print(f"{c1} x 10 = {c1*10}")