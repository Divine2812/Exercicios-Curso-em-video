#Exercício 067 - Ler o número e dizer a tabuada V3.
print('\033[33m-=' * 30 + '-\033[m')
print("\033[35mTabuada")
print('\033[33m-=' * 30 + '-\033[m')
q = 0
while True:
    n = int(input("\033[34mDigite um número:\033[m "))
    if n < 0:
        break
    for c in range(1, 10):
        l = n * c 
        q += 1
        print(f"\033[34m{n} X  {c} == \033[m{l}")
    print(f"\033[34m{n} X 10 == \033[m{n*10}")
    print('\033[m-=' * 10 + '-\033[m')
print("\033[31mPrograma finalizado!")
print('\033[33m-=' * 30 + '-\033[m')
