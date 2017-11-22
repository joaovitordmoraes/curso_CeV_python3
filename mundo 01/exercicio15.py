dias = float(input('Por quantos dias você alugou o carro? '))
km = float(input('Quantos km foram rodados? '))
rodados = km * 0.15
aluguel = (dias * 60) + rodados
print('O preço a pagar pelo carro alugado é de: R${:.2f}'.format(aluguel))

