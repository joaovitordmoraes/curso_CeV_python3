'''
     Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'.
     Caso esteja errado, peça a digitação novamente até ter um valor correto.
'''

cont = 0
while cont != 1:
    sexo = str(input('Digite o sexo: '))
    if sexo == 'M' or sexo == 'F':
        cont = cont + 1
print('Fim.')
