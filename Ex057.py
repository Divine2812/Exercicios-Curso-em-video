#Exercício 057 - Ler o sexo de uma pessoa e aceitar apenas M para masculino e F para feminino.
sexo = input("Digite o sexo de alguém: M/F ").upper()
while sexo not in 'FfMm':
    sexo = input("Informações inválidas! Digite M ou F: ").upper()
if sexo == 'M':
    seq = "Masculino"
elif sexo == 'F':
    seq = "Feminino"
print(f"Sexo {seq} registrada com sucesso!")