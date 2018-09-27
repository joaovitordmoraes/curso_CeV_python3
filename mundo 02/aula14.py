'''
for c in range (1, 11):
    print(c, end=' ')
print('Fim.')

c = 1
while c < 11:
    print(c, end=' ')
    c += 1
print('Fim.')
'''

'''
for c in range (1, 5):
    int(input('Digite um número: '))
print('Fim.')

n = 1
while n != 0:
    n = int(input('Digite um número: '))
print('Fim.')

r = 'S'
while r == 'S':
    n = int(input('Digite um número: '))
    r = str(input('Deseja continuar [S/N] ?')).upper().strip()
print('Fim.')
'''

n = 1
par = impar = 0
while n != 0:
    n = int(input('Digite um número: '))
    if n % 2 == 0:
        par += 1
    else:
        impar += 1
print('Você digitou {} números pares e {} números impares.'.format(par - 1, impar))