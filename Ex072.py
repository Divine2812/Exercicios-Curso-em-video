#Exercício 72 - Crir uma tupla com os números em extenso.
print("\033[33m -=-=-=-=-=-=-=-=-\033[m")
print("\033[35mNúmeros por extenso.")
print("\033[33m -=-=-=-=-=-=-=-=-\033[m")
ext = ('Um','Dois', 'Três','Quatro', 'Cinco', ' Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
while True:
    n = input("\033[35mDigite um número entre 0 e 20:\033[m ")
    if n.isnumeric() == False or int(n) < 0 or int(n) > 20:
        print("",end = "\033[31mNúmero inválido! Tente novamente.\033[m ")
    else: 
        print(f"\033[35mO número inserido foi {ext[(int(n)-1)].lower()}!\033[m")
        break
print("\033[33m -=-=-=-=-=-=-=-=-\033[m")