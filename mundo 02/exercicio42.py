print('-=-' * 24)
print('Digite o valor de três retas e veja se elas podem formar um triângulo')
print('-=-' * 24)

# VARIÁVEIS
a = float(input('Reta 1: '))
b = float(input('Reta 2: '))
c = float(input('Reta 3: '))

# CORES
azul = '\033[34m'
amarelo = '\033[33m'
vermelho = '\033[31m'
fecha = '\033[m'

if (b - c) < a < b + c and (a - c) < b < a + c and (a - b) < c < a + b:
    if a == b == c:
        print('Com essas três retas é possível formar um triângulo {}Equilátero{}.'.format(azul, fecha))
    elif a != b != c != a:
        print('Com essas três retas é possível formar um triângulo {}Escaleno{}'.format(vermelho, fecha))
    else:
        print('Com essas três retas é possível formar um triângulo {}Isóceles{}'.format(amarelo, fecha))

else:
    print('Com essas três retas não é possível formar um triângulo.')

