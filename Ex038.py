#Exercício 038 - Ler dois números inteiros e compare-os.
print("\033[33m-=" * 30 + "-\033[m")
print("\033[36mComparador entre dois números.")
print("\033[33m-=" * 30 + "-\033[m")
n1 = int(input("\033[36mNúmero um:\033[m "))
n2 = int(input("\033[36mNúmero dois:\033[m "))
print("\033[33m-=" * 30 + "-\033[m")
if n1 > n2:
    print(f"\033[35mO número {n1} é maior que o número {n2}!")
elif n2 > n1:
    print(f"\033[35mO número {n2} é maior que o número {n1}!")
elif n1 == n2:
    print("\033[35mOs números inseridos são iguais. =)")
print("\033[33m-=" * 30 + "-\033[m")

