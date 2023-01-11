#Exercício 041 - Seleção de jogadores
print("\033[33m-=" * 30 + "-\033[m")
print("\033[34mSeleção de categorias")
print("\033[33m-=" * 30 + "-\033[m")
id = int(input("\033[34mDigite a idade do atleta:\033[m "))
if id < 9:
    print("\033[35mIA idade inserida pertence a categoria mirim.\033[m")
elif id >= 9 and id < 14:
    print("\033[35mIA idade inserida pertence a categoria infantil.\033[m")
elif id >= 14 and id < 19: 
    print("\033[35mIA idade inserida pertence a categoria junior.\033[m")
elif id >= 19 and id < 20:
    print("\033[35mIA idade inserida pertence a categoria sênio.\033[m")
elif id > 20:
    print("\033[35mA idade inserida pertence a categoria master.\033[m")
