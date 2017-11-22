valor1 = int(input('Digite um valor: '))
valor2 = int(input('Digite outro valor: '))
soma = valor1 + valor2
multi = valor1 * valor2
div = valor1 / valor2
divint = valor1 // valor2
exp = valor1 ** valor2
print('A soma é {}, o produto é {} e a divisão é {:.3f}'.format(soma, multi, div))
print('A divisão inteira é {} e a potência é {}'.format(divint, exp))
