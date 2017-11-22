km = float(input('Qual a distância da viagem em Km? '))
gasto = km * 0.5 if km <= 200 else km * 0.45
print('O preço da sua viagem é de R${:.2f}'.format(gasto))
'''if km <= 200:
    gasto = km * 0.5
    print('O preço da sua viagem é de R${:.2f}'.format(gasto))
else:
    gasto = km * 0.45
    print('O preço da sua viagem é de R${:.2f}'.format(gasto))'''
