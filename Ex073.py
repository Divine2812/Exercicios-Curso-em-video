#Exercício 73 - Times Brasileirão
print("\033[33m-=-=-=-=-=-=-=-=-\033[m")
print("\033[35mTimes Brasileirão")
print("\033[33m-=-=-=-=-=-=-=-=-\033[m")
times = ('América - MG', 'Athletico - PR', 'Atlético - MG', 'Bahia', 'Botafogo', 'Corinthians', 'Coritiba', 'Cruzeiro', 'Cuiabá', 'Flamengo', 'Fortaleza', 'Goiás', 'Grêmio', 'Internacional', 'Palmeiras', 'Bragantino', 'Santos', 'São Paulo', 'Vasco da Gama')
print(f"Os 5 primeiros colocados são: {times[0]}", end= '')
for c in range (1,4):
    print(', ',end= str(times[c]))
print(" e " '', end=times[4] + '.\033[m\n\033[33m-=-=-=-\033[m')

print(f"\nmOs 4 últimos colocados são: \033[31m{str(times[-4])}", end= '')
for a in range (-3, -1):
    print(', ', end= str(times[a]))
print(" e " '', end=times[-1] + '.\033[m\n\033[33m-=-=-=-\033[m')
ui = (sorted(times))[1:-1]
ui = sorted(times)
print(f"\nA lista de times em ordem alfabética: \033[35m{ui[0]}",end= '')
for u in range (1, 18):
    print(', ', end= str(ui[u]))
print(' e ', end=ui[-1] + '.\033[m\n\033[33m-=-=-=-\033[m')
if 'Chapecoense' in times:
    l = times.index("Chapecoense")
    print(f"\nA Chapecoense está na {l+1}º posição.")
else: 
    print("\nA Chapecoense não ocupa nenhuma posição.")
print("\033[33m-=-=-=-=-=-=-=-=-\033[m")