#Exercício 73 - Times Brasileirão
print("\033[33m -=-=-=-=-=-=-=-=-\033[m")
print("\033[35m Times Brasileirão")
print("\033[33m -=-=-=-=-=-=-=-=-\033[m")
times = ('América - MG', 'Athletico - PR', 'Atlético - MG', 'Bahia', 'Botafogo', 'Corinthians', 'Coritiba', 'Cruzeiro', 'Cuiabá', 'Flamengo', 'Fortaleza', 'Goiás', 'Grêmio', 'Internacional', 'Palmeiras', 'Bragantino', 'Santos', 'São Paulo', 'Vasco da Gama')
print(f"Os 5 primeiros colocados são: {times[0]}", end= '')
for c in range (1,4):
    print(', ',end= str(times[c]))
print(" e " '', end=times[4])
