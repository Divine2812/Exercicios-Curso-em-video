name = ["joao", "carlos", "antonio", "pedro"]
age = ['1002', '293', '934', '2123']
if age[0] != age[1] and age[1] != age[2] and age[2] != age[3]:
    up = max(int(age))
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
