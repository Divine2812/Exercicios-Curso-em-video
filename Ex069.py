#Exercício 069 - Cadastro de pessoas
print('\033[33m-=' * 30 + '-\033[m')
print("\033[35mCadastro de pessoas")
print('\033[33m-=' * 30 + '-\033[m')
idadelista = []
sexolista = []
plus18 = men = mulheresl20 = 0
while True:
    idade = int(input("\033[34mDigite a idade da pessoa: \033[m"))
    idadelista.append(idade)
    if idade >= 18:
        plus18 += 1
    sexo = input("\033[34mDigite o sexo da pessoa: M/F \033[m").upper().strip()[0]
    while sexo not in 'M, F':
        sexo = input("\033[31mOpção inválida! Digite M ou F: \033[m").upper().strip()[0]
    sexolista.append(sexo)
    if sexo == "M":
        men += 1
    if sexo == 'F' and idade < 20:
        mulheresl20 += 1
    resposta = input("\033[34mQuer continuar? S/N \033[m").upper().strip()[0]
    while resposta not in "SN":
        resposta = input("\033[31mOpção inválida! Digite S ou N:\033[m ")
    print("-=-=-=-=-=-=-=-=-=-")
    if resposta == 'N':
        break
print(f"\033[35mHá {plus18} pessoas com mais de 18 anos, {men} homens e {mulheresl20} mulheres com menos de 20 anos.")
print('\033[33m-=' * 30 + '-\033[m')