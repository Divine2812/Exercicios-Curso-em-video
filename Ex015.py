#Exercício 15 - Ver a quantidade de dias que um carro foi alugado e a quantidade de KMs percorridos
#fazer a fórmula a ser paga.
Dias = int(input("Quantos dias o carro foi utilizado? "))
Km = float(input("Quantos Kms foram percorridos com o carro? "))
Vdia = Dias*60
VKm = Km*0.15
print(f"O valor a ser pago, considerando {Dias} dias e {Km} Kms, será de {Vdia+VKm:.2f} R$!")
