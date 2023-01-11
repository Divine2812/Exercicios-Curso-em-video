#Exercício 040 - Calcular a média de um aluno 2.0
print("\033[33m-=" * 30 + "-\033[m")
print("\033[34mCalcular a média e saber se o aluno está aprovado, em recuperação ou reprovado.")
print("\033[33m-=" * 30 + "-\033[m")
n1 = float(input("\033[34mDigite a primeira nota: \033[m"))
n2 = float(input("\033[34mDigite a segunda nota: \033[m"))
m = (n1+n2)/2
if m < 5:
    print(f"\033[35mInfelizmente você não foi aprovado, sua média ficou abaixo de 5.\nMédia: {m}\033[m")
elif m == 5 or m > 5 and m < 6.9:
    print(f"\033[35mSua média foi de {m}, você está em recuperação!\033[m")
elif m >= 7:
    print(f"\033[35mVocê obteve média {m} e foi aprovado! Parabéns.\033[m")