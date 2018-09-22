'''
    CRIE UM PROGRAMA QUE LEIA O ANO DE NASCIMENTO DE SETE PESSOAS.
    NO FINAL, MOSTRE QUANTAS PESSOAS AINDA NÃO ATINGIRAM A MAIORIDADE
    E QUANTAS JÁ SÃO MAIORES DE IDADE.
'''
from datetime import datetime
maior = 0
menor = 0
anoatual = datetime.now().year
for c in range(1, 8):
    nascimento = int(input('Digite o {} ano de nascimento: '.format(c)))
    if anoatual - nascimento >= 18:
        maior += 1
    else:
        menor += 1
print('Das datas de nascimento digitadas {} são maiores de idade e {} são menores de idade.'.format(maior, menor))
