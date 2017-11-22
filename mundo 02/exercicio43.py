print('-=-' * 5)
print('Cálculo do IMC')
print('-=-' * 5)

peso = float(input('Digite o seu peso(Kg): '))
altura = float(input('Digite sua altura(m): '))

imc = peso / (altura * altura)

if imc < 18.5:
    print('Você está abaixo do peso.')
elif (imc >= 18.5) and (imc < 25):
    print('Você está no peso ideal.')
elif (imc >= 25 ) and (imc < 30):
    print('Você está em sobrepeso.')
elif (imc >= 30) and (imc <= 40):
    print('Você está em obesidade.')
else:
    print('Você está em obesidade mórbida.')
