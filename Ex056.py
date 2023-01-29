#Exercício 056 - Ler o nome, sexo e idade de 4 pessoas e no final mostrar a média de idade do grupo, nome do homem mais velho e a quantidade de mulheres que tem menos de 20 anos.
print('\033[33m-=' * 30 + '-\033[m')
print('\033[35mAnalisador de dados')
print('\033[33m-=' * 30 + '-\033[m')
age = []
sex = []
name = []
s = ""
a = ""
for pg in range (0, 4):
    u = pg + 1
    if u == 1:
        org = "primeira"
    elif u == 2:
        org = "segunda"
    elif u == 3:
        org = "terceira"
    elif u == 4:
        org = "quarta" #organiza as palavras "primeira, "Segunda, "Terceira" e "Quarta" nas frases input.
    n = str(input(f"\033[34mDigite o nome da {org} pessoa:\033[m "))
    while s.lower().strip() != "masculino" or s.lower().strip() != "feminino": #Só aceita masculino e feminino como input.
        s = input(f"\033[34mDigite o sexo da {org} pessoa: Mas/Fem \033[m")
        if s.lower().strip() == "masculino":
            sex.append(s)
            break
        elif s.lower().strip() == "feminino":
            sex.append(s)
            break
        else: 
            print("\033[31mO sexo informado não corresponde à nenhuma opção programada. Digite masculino ou feminino.")
    while a.isnumeric() == False and len(a) < 4: #Só aceita números
        a = (input(f"\033[34mDigite a idade da {org} pessoa: \033[m"))
        if a.isdigit() == True:
            age.append(int(a))
            a = "" #Se não resetar a variável, o programa pede a idade apenas na primeira vez
            break
        else:
            print("\033[31mIdade inválida! Digite apenas números.")
    name.append(n)
print("\033[m-=-=-=-")
med = (int(age[0]) + int(age[1]) + int(age[2]) + int(age[3])) / 4  #média das idades
print(f"\033[35mA média de idade entre as pessoas inseridas é {med}")
print("\033[m-=-=-=-")
if age[0] == age[1] and age[1] == age[2] and age[2] == age[3]: #If e elif para organizar caso tenha mais de uma pessoa com idades iguais. 
    print("\033[35mAs pessoas tem a mesma idade.")
elif age[0] != age[1] and age[1] != age[2] and age[2] != age[3]:
    up = max(age)
    loc = age.index(up)
    if loc == 0:
        nome_age = name[0]
        print(f"\033[35mA pessoa mais velha é {nome_age} com {up} anos.")
    elif loc == 1:
        nome_age = name[1]
        print(f"\033[35mA pessoa mais velha é {nome_age} com {up} anos.")
    elif loc == 2:
        nome_age = name[2]
        print(f"\033[35mA pessoa mais velha é {nome_age} com {up} anos.")
    elif loc == 3:
        nome_age = name[3]
        print(f"\033[35mA pessoa mais velha é {nome_age} com {up} anos.")
elif age[0] == age[1]:
    print(f"\033[35mAs pessoas {name[0]} e {name[1]} tem a mesma idade, {age[0]} anos.")
elif age[1] == age[2]:
    print(f"\033[35mAs pessoas {name[1]} e {name[2]} tem a mesma idade, {age[1]} anos.")
elif age[2] == age[3]:
     print(f"\033[35mAs pessoas {name[2]} e {name[3]} tem a mesma idade, {age[2]} anos.")
elif age[0] == age[3]:
    print(f"\033[35mAs pessoas {name[0]} e {name[3]} tem a mesma idade, {age[0]} anos.")
elif age[1] == age[3]:
    print(f"\033[35mAs pessoas {name[1]} e {name[3]} tem a mesma idade, {age[1]} anos.")
elif age[0] == age[2]:
    print(f"\033[35mAs pessoas {name[0]} e {name[2]} tem a mesma idade, {age[0]} anos.")
print("\033[m=-=-=-")
qnt_woml20 = 0 #Ver quantas mulheres tem menos de 20 anos.
if sex[0] == 'feminino' and int(age[0]) < 20:
    qnt_woml20 = qnt_woml20 + 1
    if sex[1] == 'feminino' and int(age[1]) < 20:
        qnt_woml20 = qnt_woml20 + 1
        if sex[2] == 'feminino' and int(age[2]) < 20:
            qnt_woml20 = qnt_woml20 + 1
            if sex[3] == 'feminino' and int(age[3]) < 20:
                qnt_woml20 = qnt_woml20 + 1
if qnt_woml20 == 1:
    print(f"\033[35mHá {qnt_woml20} mulher com menos de 20 anos!")
elif qnt_woml20 >= 2:
    print(f"\033[35mHá {qnt_woml20} mulheres com menos de 20 anos!")
else: 
    print(f"\033[35mNão há nenhuma mulher com menos de 20 anos!")
print('\033[33m-=' * 30 + '-\033[m')