'''
    Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
    O programa será interrompido quando o número solicitado for negativo.
'''
n = m = 0
cont = 1
while True:
    n = int(input('Quer ver a tabuada de qual valor? '))
    if n > 0:
        while cont <= 10:
            m = n * cont
            print(f'{n} x {cont} = {m}')
            cont += 1
        cont = 1
    else:
        break
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')
