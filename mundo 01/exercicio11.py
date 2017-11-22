base = float(input('Digite quantos metros a parede tem de largura: '))
altura = float(input('Digite quantos metros a parede tem de altura: '))
area = base * altura
quantidade = area / 2
print('A parede possui {} metros quadrados. Será necessário {} litros de tinta para pintar esta parede.'.format(area, quantidade))

