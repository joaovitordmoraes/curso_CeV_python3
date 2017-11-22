velocidade = float(input('Digite a velocidade do carro: '))
if velocidade <= 80:
    print('Você está dentro do limite de velocidade, parabéns!')
else:
    print('Você está {}km/h acima da velocidade permitida.'.format(velocidade - 80))
    multa = (velocidade - 80) * 7
    print('Você levou uma multa de R${:.2f}'.format(multa))
