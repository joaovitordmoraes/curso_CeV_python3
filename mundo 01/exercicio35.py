print('-=-' * 24)
print('Digite o valor de três retas e veja se elas podem formar um triângulo')
print('-=-' * 24)
a = float(input('Reta 1: '))
b = float(input('Reta 2: '))
c = float(input('Reta 3: '))
if (b - c) < a < b + c and (a - c) < b < a + c and (a - b) < c < a + b:
    print('Com essas três retas é possível formar um triângulo.')
else:
    print('Com essas três retas não é possível formar um triângulo.')

