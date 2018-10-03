'''
    Escreva um programa que leia um número N inteiro qualquer e mostre
    na tela os N primeiros elementos de uma Sequência de Fibonacci.
'''
n = int(input('Digite um número qualquer: '))
cont = 3
fib = 0
t1 = 0
t2 = 1
print('{} -> {}'.format(t1, t2), end='')
while cont <= n:
    fib = t1 + t2
    print(' -> {}'.format(fib), end='')
    t1 = t2
    t2 = fib
    cont += 1
print(' -> Fim.')
