inicial = int(input('Digite o número inicial da PA: '))
r = int(input('Digite a razão da PA: '))
pa = inicial + (10 - 1) * r
for c in range (inicial, pa + r, r):
    print('{}'.format(c), end=" -> ")
print('FIM.')