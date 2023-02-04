#Exercício 065 - Ler vários números e informar a média, menor valor e o maior valor entre eles.
print('\033[33m-=' * 30 + '-\033[m')
print("\033[35mMédia entre números")
print('\033[33m-=' * 30 + '-\033[m')
numeroescolha = 0
contador = 0
n = 0
soma = 0
lista = []
escolha = []
while escolha != 'N':
    n = int(input("\033[34mDigite um número:\033[m "))
    lista.append(n)
    contador += 1
    soma += n 
    escolha = input("\033[34mDeseja continuar? S/N\033[m ").upper()
print(f"\033[35mA quantidade de números inseridos foi {contador};\nA média entre eles é de {soma/contador:.2f};\nO maior valor é {max(lista)} e o menor valor é {min(lista)}! =)")
print('\033[33m-=' * 30 + '-\033[m')