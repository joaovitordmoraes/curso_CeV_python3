numero = int(input('Digite um número inteiro: '))
print('Escolha para qual base você deseja converter.')
print('Digite [1] para Binário')
print('Digite [2] para Octal')
print('Digite [3] para Hexadecimal')
escolha = int(input('Digite o número: '))

if escolha == 1:
    print('Esse número em Binário fica: {}'.format(bin(numero)[2:]))
elif escolha == 2:
    print('Esse número em Octal fica: {}'.format(oct(numero)[2:]))
elif escolha == 3:
    print('Esse número em Hexadecimal fica: {}'.format(hex(numero)[2:]))
else:
    print('Base inválida!')
