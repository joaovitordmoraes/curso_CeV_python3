from math import hypot

oposto = float(input('Digite o valor do cateto oposto: '))
adj = float(input('Digite o valor do cateto adjacente: '))
hipotenusa = hypot(oposto, adj)
print('O valor da hipotenusa é {:.2f}'.format(hipotenusa))
