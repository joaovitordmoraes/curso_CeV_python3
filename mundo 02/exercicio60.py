'''
    Faça um programa que leia um número qualquer e mostre o seu fatorial.
'''
n = int(input('Digite um número para \ncalcular seu Fatorial: '))
multiplicacao = 1
print('O fatorial de {} é:'.format(n))
while n != 0:
    multiplicacao = multiplicacao * n
    print('{} '.format(n), end='')
    print('x ' if n > 1 else '= ', end='')
    n = n - 1
print(multiplicacao)