num = int(input('Digite um número: '))
cores = {'fecha': '\033[m',
         'vermelho': '\033[0;31m',
         'verde': '\033[0;32m'}

for c in range(1, num+1, 1):
    if num % c == 0:
        print('{}'.format(cores['verde']), end='')
    else:
        print('{}'.format(cores['vermelho']), end='')
    print('{} '.format(c), end='')
print('{}'.format(cores['fecha']))
if num % 2 == 1:
    print('O número {} é primo'.format(num))
else:
    print('O número {} não é primo'.format(num))