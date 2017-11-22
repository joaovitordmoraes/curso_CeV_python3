s = 0
for c in range(1, 7, 1):
    n = int(input('Digite um número: '))
    if n % 2 == 0:
        s += n
print('A soma dos números pares digitados é de {}'.format(s))
