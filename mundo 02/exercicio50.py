s = 0
for c in range(0, 6, 1):
    n = int(input('Digite o {} número: '.format(c)))
    if n % 2 == 0:
        s += n
if s <= 0:
    print('Não foi digitado nenhum número par.')
else:
    print('A soma dos números pares apresentados foi de: {}' .format(s))
