from time import sleep
print('\033[33m-=' * 10 + '-\033[m')
print("\033[35m     Calculadora")
print('\033[33m-=' * 10 + '-\033[m')
numero01 = float(input("Digite um número: "))
numero02 = float(input("Digite um número: "))
print('\033[33m-=' * 10 + '-\033[m')
print(f"Certo! Os números digitados são {numero01} e {numero02}. \nAgora, escolha uma opção abaixo: ")
print('\033[33m-=' * 10 + '-\033[m')
numero_escolhido = ''
while numero_escolhido != 6:
    numero_escolhido = int(input("""\033[36mDigite \033[31m[1] \033[36mpara somar os números;
Digite \033[31m[2] \033[36mpara subtrair os números;
Digite \033[31m[3] \033[36mpara multiplicar
Digite \033[31m[4] \033[36mpara obter o maior número inserido;
Digite \033[31m[5] \033[36mpara adicionar novos números;
Digite \033[31m[6] \033[36mpara sair do programa;
\033[33m-=-=-=-=-=-=-=-=-=-=-
\033[35mDigite a opção desejada: \033[m"""))
    if numero_escolhido == 1:
        sleep(1)
        print("Carregando...")
        sleep(1)
        print(f"Somando os valores {numero01} e {numero02}, o resultado é: {numero01 + numero02}!")
        print('\033[33m-=' * 10 + '-\033[m')
        sleep(1)
    elif numero_escolhido == 2:
        sleep(1)
        print("Carregando...")
        sleep(1)
        print(f"Subtraindo os valores {numero01} e {numero02}, o resultado é: {numero01 - numero02}!")
        print('\033[33m-=' * 10 + '-\033[m')
        sleep(1)
    elif numero_escolhido == 3:
        sleep(1)
        print("Carregando...")
        sleep(1)
        print(f"Multiplicando o valor {numero01} por {numero02}, o resultado é: {numero01 * numero02}")
        print('\033[33m-=' * 10 + '-\033[m')
        sleep(1)
    elif numero_escolhido == 4: 
        sleep(1)
        print("Carregando...")
        print(f"O maior valor entre {numero01} e {numero02} é o {max(numero01, numero02)}!")
        print('\033[33m-=' * 10 + '-\033[m')
        sleep(1)               
    elif numero_escolhido == 5:
        numero01 = int(input("Digite um número: "))
        numero02 = int(input("Digite um número: "))
    elif numero_escolhido == 6:
        sleep(1)
        print("Carregando...")
        sleep(1)
        print(f"Ok! Finalizando...")
        print('\033[33m-=' * 10 + '-\033[m')
        exit()
    elif numero_escolhido > 6:
        print("Opção inválida! Por favor, escolha apenas os números entre 1 a 6.")
        
