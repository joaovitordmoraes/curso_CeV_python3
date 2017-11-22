print('\033[4;30;45mOlá, Mundo!\033[m')
print('\033[7;30mOlá, Mundo!\033[m')
s = 'Sim'
n = 'Não'
print('Você diz muito \033[32m{}\033[m, precisa dizer mais \033[31m{}\033[m'.format(s, n))
nome = 'João'
print('Olá, muito prazer em te conhecer, {}{}{}'.format('\033[34m', nome, '\033[m'))
cores = {'limpa': '\033[m',
         'azul': '\033[34m',
         'amarelo': '\033[33m',
         'pb': '\033[7;30m'}
print('Olá, muito prazer em te conhecer, {}{}{}'.format(cores['amarelo'], nome, cores['limpa']))
