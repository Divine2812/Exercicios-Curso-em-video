#Exercício 043 - Calcular o IMC e informar se a pessoa está com o seu peso ideal alterado. 
print('\033[33m-=' * 30 + '-\033[m')
print("\033[36mCalculadora de IMC - Indíce de massa corporal")
print('\033[33m-=' * 30 + '-\033[m')
hal = float(input("\033[36mPara começarmos, digite sua altura: "))
pes = float(input("\033[36mEm seguida, digite seu peso: "))
imc = pes / (hal * hal)
if imc < 18.5: 
    print(f"\033[35mO seu IMC é de {imc:.2f}, você está abaixo do peso!\033[m")
elif imc >= 18.5 and imc < 25:
    print(f"\033[35mO seu IMC é de {imc:.2f}, você está no seu peso ideal!\033[m")
elif imc > 25 and imc < 30:
    print(f"\033[35mO seu IMC é de {imc:.2f}, você está com sobrepeso!\033[m")
elif imc > 30 and imc < 40:
    print(f"\033[35m seu IMC é de {imc:.2f}, você está com obesidade!\033[m")
elif imc >= 40:
    print(f"\033[35mO seu IMC é de {imc:.2f}, você está com obesidade mórbida!\033[m")
print('-=' * 30 + '-')
